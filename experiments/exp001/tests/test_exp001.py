import json
import tempfile
import unittest
import io
import os
from unittest.mock import patch
from pathlib import Path
from types import SimpleNamespace
from exp001.core import load_cases, eligible,ranked, score, validate_response
from exp001.evaluation import load_private_key,evaluate
from exp001.llm import MockModel, OpenAIResponsesModel, PROPOSAL_SCHEMA
from exp001.cli import run
BASE=Path(__file__).resolve().parents[1]

class ExperimentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases,cls.digest=load_cases(BASE/'data/scenarios.json')
        private=BASE/'data/private/answer_key.json'
        cls.key=load_private_key(private) if private.exists() else None
    def test_source_schema_and_phase(self):
        self.assertEqual(len(self.cases),35)
        self.assertEqual(len([c for c in self.cases if c['phase']=='calibracao']),5)
        self.assertEqual(len([c for c in self.cases if c['phase']=='principal']),30)
        if self.key is not None:
            self.assertEqual(sum(self.key[c['id']]['class']=='prejudicial' for c in self.cases if c['phase']=='principal'),10)
        self.assertTrue(len(self.digest)==64)
    def test_private_key_matches_public_rules(self):
        if self.key is None: self.skipTest('Chave privada não incluída na versão pública')
        for c in self.cases:
            scores=[score(c,o) for o in ranked(c)]
            self.assertTrue(scores,c['id'])
            best_score=scores[0]
            acceptable={o['id'] for o in ranked(c) if abs(score(c,o)-best_score)<1e-8}
            self.assertEqual(acceptable,set(self.key[c['id']]['best_ids']),c['id'])
    def test_calibration_expected(self):
        expected={'CAL-01':['A'],'CAL-02':['A','B'],'CAL-03':['C'],'CAL-04':['A'],'CAL-05':['C']}
        for cid,ids in expected.items():
            c=next(c for c in self.cases if c['id']==cid)
            best=score(c,ranked(c)[0])
            computed=[o['id'] for o in ranked(c) if abs(score(c,o)-best)<1e-8]
            self.assertEqual(computed,ids)
            if self.key is not None: self.assertEqual(self.key[cid]['best_ids'],ids)
    def test_no_key_in_public_dataset(self):
        content=(BASE/'data/scenarios.json').read_text(encoding='utf8')
        self.assertNotIn('best_ids',content)
        self.assertNotIn('prejudicial',content)
        self.assertNotIn('negative_control',content)
    def test_mock_three_conditions(self):
        c=next(c for c in self.cases if c['id']=='CAL-03')
        model=MockModel()
        proposals={}
        for condition in 'ABC':
            initial,_=model.propose(c,condition)
            if condition=='C':
                critique,_=model.contest(c,initial)
                final,_=model.propose(c,condition,critique)
            else:final=initial
            proposals[condition]=final
            best=score(c,ranked(c)[0])
            reference={'best_ids':[o['id'] for o in ranked(c) if abs(score(c,o)-best)<1e-8]}
            self.assertEqual(evaluate(c,final,reference)['eligible_choice'],True)
        self.assertEqual(proposals['C']['recommended_id'],'C')
    def test_api_plan_without_credentials(self):
        with tempfile.TemporaryDirectory() as tmp:
            args=SimpleNamespace(public='',private='',mode='openai',model='modelo_exemplo',phase='calibration',
                 limit=1,repeats=1,seed=20261013,output=str(Path(tmp)/'resultado'),conditions='ABC',
                 max_api_calls=5,dry_run=True)
            plan=run(args)
            self.assertEqual(plan['api_calls_planned'],5)
            self.assertEqual(plan['responses_planned'],3)
            self.assertFalse(Path(args.output).exists())

    def test_api_limit_prevents_network_and_file_creation(self):
        with tempfile.TemporaryDirectory() as tmp:
            args=SimpleNamespace(public='',private='',mode='openai',model='modelo_exemplo',phase='calibration',
                 limit=2,repeats=1,seed=20261013,output=str(Path(tmp)/'resultado'),conditions='ABC',
                 max_api_calls=5,dry_run=False)
            with self.assertRaisesRegex(ValueError,'exige 10 chamadas'):
                run(args)
            self.assertFalse(Path(args.output).exists())

    def test_existing_results_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)/'run'; target.mkdir()
            (target/'sentinela.txt').write_text('proteger')
            args=SimpleNamespace(public='',private='',mode='mock',model='',phase='calibration',
                 limit=1,repeats=1,seed=20261013,output=str(target),conditions='A')
            with self.assertRaises(FileExistsError):run(args)
            self.assertEqual((target/'sentinela.txt').read_text(),'proteger')

    def test_api_request_contract_mocked_no_network(self):
        response={'status':'completed','id':'resp_test','output':[{'type':'message',
            'content':[{'type':'output_text','text':json.dumps({'recommended_id':'A'})}]}],
            'usage':{'input_tokens':100,'output_tokens':50}}
        captured=[]
        def fake_open(request,timeout=120):
            captured.append(json.loads(request.data.decode('utf8')))
            return io.BytesIO(json.dumps(response).encode('utf8'))
        with patch.dict(os.environ,{'OPENAI_API_KEY':'CHAVE_SIMULADA'},clear=False):
            client=OpenAIResponsesModel('modelo_de_teste')
            with patch('urllib.request.urlopen',side_effect=fake_open):
                result,meta=client._query('proposta',PROPOSAL_SCHEMA,'instrucoes',{'case':'sintetico'})
        self.assertEqual(result['recommended_id'],'A')
        self.assertEqual(meta['input_tokens'],100)
        self.assertFalse(captured[0]['store'])
        self.assertEqual(captured[0]['text']['format']['type'],'json_schema')
        self.assertEqual(captured[0]['max_output_tokens'],2500)

    def test_api_rejects_incomplete_response(self):
        reply={'status':'incomplete','output':[{'type':'message',
            'content':[{'type':'output_text','text':'{"recommended_id":"A"}'}]}]}
        with patch.dict(os.environ,{'OPENAI_API_KEY':'CHAVE_SIMULADA'},clear=False):
            client=OpenAIResponsesModel('modelo_de_teste')
            with patch('urllib.request.urlopen',return_value=io.BytesIO(json.dumps(reply).encode('utf8'))):
                with self.assertRaisesRegex(RuntimeError,'não foi concluída'):
                    client._query('proposta',PROPOSAL_SCHEMA,'instrucoes',{'case':'sintetico'})

    def test_invalid_model_option_blocked(self):
        c=next(c for c in self.cases if c['id']=='CAL-01')
        val,_=MockModel().propose(c,'A')
        val['recommended_id']='ZZ'
        with self.assertRaises(ValueError): validate_response(c,val)
    def test_end_to_end_calibration_mock(self):
        with tempfile.TemporaryDirectory() as tmp:
            args=SimpleNamespace(public='',private='',mode='mock',model='',phase='calibration',
                 limit=0,repeats=1,seed=20261013,output=tmp,conditions='ABC')
            summary=run(args)
            self.assertEqual(summary['records'],15)
            self.assertTrue((Path(tmp)/'full_traces_private.jsonl').exists())
            traces=[json.loads(line) for line in (Path(tmp)/'full_traces_private.jsonl').read_text().splitlines()]
            self.assertEqual(len([t for t in traces if t['condition']=='C']),5)
            self.assertTrue(all(len(t['stages'])==3 for t in traces if t['condition']=='C'))
            blinded=(Path(tmp)/'reviewer_masked.jsonl').read_text()
            self.assertNotIn('"condition"',blinded)
            self.assertNotIn('"metrics"',blinded)
            self.assertNotIn('"premises"',blinded)
            self.assertNotIn('"stages"',blinded)

if __name__=='__main__':unittest.main()
