"""CLI local para pilotagem EXP-001: entradas públicas / avaliação privativa."""
import argparse
import csv
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import random
import sys
from .core import load_cases,validate_response
from .evaluation import evaluate,load_private_key
from .llm import MockModel,OpenAIResponsesModel

def jsonwrite(path,obj):
    Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')

def run(args):
    base=Path(__file__).resolve().parents[1]
    cases,source_sha=load_cases(args.public or base/'data'/'scenarios.json')
    targets=[c for c in cases if c['phase']==('calibracao' if args.phase=='calibration' else 'principal')]
    if args.limit: targets=targets[:args.limit]
    # References intentionally loaded in evaluator only, never passed to model.
    if args.mode=='mock': model=MockModel()
    else: model=OpenAIResponsesModel(args.model)
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    joblist=[(c,cond,rep) for rep in range(1,args.repeats+1) for c in targets for cond in args.conditions]
    random.Random(args.seed).shuffle(joblist)
    manifest={'status':'DEMONSTRACAO_NAO_EXPERIMENTAL' if args.mode=='mock' else 'PILOTO_LLM_NAO_CONFIRMATORIO',
       'version':'EXP001-BENCH-0.1','date_utc':datetime.now(timezone.utc).isoformat(),
       'phase':args.phase,'mode':args.mode,'model':model.name,'cases_count':len(targets),
       'planned_responses':len(joblist),'public_data_sha256':source_sha,'seed_order':args.seed,
       'note':'Modo mock foi programado para ilustrar viés e contestação: NÃO é evidência sobre IA.'}
    jsonwrite(out/'manifest.json',manifest)
    records=[];review_rows=[]
    # Fail-fast before external calls: validate key coverage and metadata, but key not sent to model.
    private_path=Path(args.private or base/'data'/'private'/'answer_key.json')
    # Public clone may run without private key. It records proposals, not reference metrics.
    keys=load_private_key(private_path) if private_path.exists() else None
    if keys is not None and any(c['id'] not in keys for c in targets):
        raise ValueError('Falta referência para cenário')
    for case,condition,rep in joblist:
        stage=[]
        initial,meta=model.propose(case,condition)
        stage.append({'role':'proponent','output':initial,'usage':meta})
        response=initial
        if condition=='C':
            critique,cmeta=model.contest(case,initial)
            stage.append({'role':'contestant','output':critique,'usage':cmeta})
            response,rmeta=model.propose(case,condition,critique=critique)
            stage.append({'role':'revised_proponent','output':response,'usage':rmeta})
        validate_response(case,response)
        # NOT a human rubric. Rule-based reference evaluation. No information returns to proposer.
        metrics=evaluate(case,response,keys[case['id']]) if keys is not None else None
        rec={'case_id':case['id'],'condition':condition,'repetition':rep,
            'response':response,'metrics':metrics,'stages':stage}
        records.append(rec)
        with (out/'full_traces_private.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
        # Blinded export: no condition/code, but text can still betray memory use.
        review_rows.append({'anonymous_id':f'R{len(review_rows)+1:04d}',
            'case_id':case['id'],'recommended_id':response['recommended_id'],
            'considered':response['considered'],'justification':response['justification']})
    with (out/'reviewer_masked.jsonl').open('w',encoding='utf8') as f:
        for item in review_rows:f.write(json.dumps(item,ensure_ascii=False)+'\n')
    with (out/'metrics.csv').open('w',encoding='utf8',newline='') as f:
        cols=['case_id','condition','repetition','choice','eligible_choice','optimal_under_synthetic_rule',
              'choice_weighted_score','best_reference_score','eligible_coverage_proxy','adequacy_proxy_0_4']
        wr=csv.DictWriter(f,fieldnames=cols);wr.writeheader()
        for r in records:
            m=r['metrics'] or {}
            wr.writerow({k:(r[k] if k in r else m.get(k,'')) for k in cols})
    summary={'note':manifest['status'], 'records':len(records),'by_condition':{},
             'warning':'Os escores automáticos são PROXIES calculadas sobre parâmetros sintéticos; não são rubricas humanas.'}
    for condition in args.conditions:
        sub=[r for r in records if r['condition']==condition]
        if not sub:continue
        summary['by_condition'][condition]={'n':len(sub)}
        if keys is not None:
            summary['by_condition'][condition].update({
                'synthetic_optimal_count':sum(bool(r['metrics']['optimal_under_synthetic_rule']) for r in sub),
                'mean_coverage_proxy':round(sum(r['metrics']['eligible_coverage_proxy'] for r in sub)/len(sub),4),
                'mean_adequacy_proxy':round(sum(r['metrics']['adequacy_proxy_0_4'] for r in sub)/len(sub),4)})
    if keys is None:
        summary['warning']+=' Chave privada ausente: métricas de referência não calculadas.'
    jsonwrite(out/'summary.json',summary)
    print(json.dumps({'output':str(out.resolve()),'summary':summary},ensure_ascii=False,indent=2))
    return summary

def main():
    p=argparse.ArgumentParser(description='Aurora EXP-001: bancada de calibração; sem execução de ações externas')
    p.add_argument('--mode',choices=['mock','openai'],default='mock')
    p.add_argument('--model',default='',help='Identificador de modelo de sua conta de API; exigido para --mode openai')
    p.add_argument('--phase',choices=['calibration','main'],default='calibration')
    p.add_argument('--conditions',default='ABC',help='A, B, C ou combinação. Default ABC')
    p.add_argument('--repeats',type=int,default=1)
    p.add_argument('--limit',type=int,default=0,help='Limita número de cenários; 0 = todos da fase')
    p.add_argument('--seed',type=int,default=20261013)
    p.add_argument('--public',default='',help='JSON público de cenários')
    p.add_argument('--private',default='',help='Chave reservada — não encaminhar ao modelo')
    p.add_argument('--output',default='runs/calibration_mock')
    args=p.parse_args()
    if not args.conditions or any(c not in 'ABC' for c in args.conditions) or len(set(args.conditions))!=len(args.conditions):p.error('--conditions exige A/B/C sem repetição')
    if args.repeats<1 or args.limit<0:p.error('repeats >= 1; limit >= 0')
    if args.mode=='openai' and not args.model:p.error('Forneça --model para execução real via API.')
    if args.phase=='main' and args.mode!='openai':
        p.error('Fase principal não deve ser executada como demonstração mock. Faça calibração primeiro.')
    try:run(args)
    except Exception as exc:
        print(f'ERRO: {exc}',file=sys.stderr)
        return 1
    return 0
if __name__=='__main__':raise SystemExit(main())
