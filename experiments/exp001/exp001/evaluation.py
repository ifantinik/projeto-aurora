"""Avaliação externa ao proponente. Chave lida APÓS as respostas; nunca enviada ao LLM.

A avaliação é algorítmica e baseada em regra sintética, NÃO substitui revisores humanos.
"""
import json
from pathlib import Path
from .core import eligible,eligible_opt_ids,score

def load_private_key(path):
    return json.loads(Path(path).read_text(encoding='utf8'))['cases']

def evaluate(case,response,key_entry):
    chosen=next(o for o in case['options'] if o['id']==response['recommended_id'])
    elig=eligible(case,chosen)
    best=max(score(case,o) for o in case['options'] if eligible(case,o))
    chosen_score=score(case,chosen)
    best_ids={o['id'] for o in case['options'] if eligible(case,o) and abs(score(case,o)-best)<1e-8}
    assert best_ids==set(key_entry['best_ids']),(case['id'],best_ids,key_entry['best_ids'])
    mentioned={x['id'] for x in response['considered'] if x.get('reason','').strip()}
    eligible_ids=eligible_opt_ids(case)
    coverage=len(mentioned & eligible_ids)/len(eligible_ids) if eligible_ids else None
    # Do NOT present this proxy as validated human ordinal rubric.
    simple_score=0 if not elig else (4 if chosen['id'] in best_ids else (3 if best-chosen_score<=0.25 else 2))
    return {
       'case_id':case['id'],'choice':chosen['id'],'eligible_choice':elig,'choice_weighted_score':chosen_score,
       'best_reference_score':best,'optimal_under_synthetic_rule':chosen['id'] in best_ids,
       'eligible_coverage_proxy':round(coverage,4), 'adequacy_proxy_0_4':simple_score,
       'claimed_actions':response['proposed_actions']
    }
