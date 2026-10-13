# Projeto Aurora — Óruias | Bancada EXP-001 (v0.1.1)

**Status:** bancada experimental funcional; **não é o agente Óruias final e não demonstra a hipótese sobre BIAS**.

> Uma arquitetura relacional não deveria apenas aprender com aquilo que se repete. Deveria também permitir investigar aquilo que a repetição tornou invisível.

## O que está implementado

- Leitura de **35 cenários sintéticos**: 5 de calibração revisados (v0.2) e 30 principais originais.
- Três condições com dados idênticos, exceto informação de memória e procedimento de contestação:
  - **A:** proposta sem memória histórica.
  - **B:** proposta com memória sintética de preferência por soluções open source, que **não é regra autorizada**.
  - **C:** proposta com memória → contestação explícita → nova proposta.
- Dois executores: `mock` determinístico **apenas para validar o software**, e `openai` para chamadas reais à API.
- Avaliação algorítmica fora do proponente, usando gabarito separado **quando disponível**; grava logs e resultados. A versão pública roda sem gabarito, mas sem métricas de referência.
- Exportação mascarada para revisores, **com cegamento ainda imperfeito** (linguagem de memória pode permanecer nas justificativas).
- Gate de segurança: nenhuma ferramenta de escrita, mutação ou execução de ações é fornecida ao modelo.

## Estrutura

```text
projeto_aurora_exp001_v0_1/
├── exp001/
│   ├── __init__.py
│   ├── core.py          # schemas, pesos, elegibilidade e validação
│   ├── llm.py           # mock / modelo proponente / contestação (API opcional)
│   ├── evaluation.py    # leitura privativa da chave e métricas determinísticas
│   └── cli.py           # execução, rastros, anonimização parcial e resumo
├── data/
│   ├── scenarios.json  # dados públicos: pode ser fornecido ao modelo
│   └── private/
│       └── answer_key.json  # NÃO ENVIAR ao modelo; reservar aos avaliadores
├── tests/
│   └── test_exp001.py
├── docs/
│   └── DECISOES_E_LIMITES.md
└── runs/                # saídas geradas localmente
```

## Testar sem credenciais e sem gabarito (recomendado primeiro)

Use Python 3.10+ (somente biblioteca padrão), na pasta raiz:

```bash
python -m unittest discover -s tests -v
python -m exp001.cli --mode mock --phase calibration --conditions ABC --repeats 1 --output runs/calibracao_mock
```

No pacote público, os testes que exigem a chave reservada serão ignorados; a execução gera rastros e não calcula métricas de referência. A chave permanece no Drive em área reservada. Para avaliar com ela, informe `--private CAMINHO_DA_CHAVE` sem copiá-la ao repositório.

O `mock` implementa de propósito uma regra simplificada e artificial: **adiciona um bônus de 0,60 à pontuação de soluções abertas quando vê a memória histórica; a etapa de contestação retira esse bônus**. Ele serve para verificar se proposta, contestação, logs e avaliador conversam entre si. **Números do mock não são evidências de redução de viés em LLMs.**

## Verificar plano de chamadas antes de qualquer custo

O planejamento não precisa de credenciais nem cria arquivos:

```bash
python -m exp001.cli --mode openai --model MODELO_DISPONIVEL --phase calibration --limit 1 --conditions ABC --dry-run
```

Para 1 cenário em A/B/C, a bancada prevê **3 respostas e 5 chamadas** (C contém proposta, contestação e revisão). O limite padrão `--max-api-calls 5` impede executar acidentalmente muitos casos; ampliá-lo exige passar o parâmetro explicitamente. O máximo por chamada é 2.500 tokens de saída, mas **não há previsão fechada do custo monetário**, pois faltam o modelo, seu preço e os tokens de entrada. Resultados anteriores nunca são sobrescritos: use um diretório `--output` novo por rodada.

## Rodar uma calibração REAL com modelo de linguagem

Uma vez definidos o modelo disponível na sua conta de API e o orçamento, configure a variável de ambiente **localmente** (não inclua a chave em arquivos enviados ou no GitHub):

```bash
# Linux/macOS
export OPENAI_API_KEY='sua_chave_aqui'
python -m exp001.cli --mode openai --model NOME_DO_MODELO --phase calibration --limit 1 --repeats 1 --output runs/piloto_api_1
```

No Windows PowerShell:

```powershell
$env:OPENAI_API_KEY = 'sua_chave_aqui'
python -m exp001.cli --mode openai --model NOME_DO_MODELO --phase calibration --limit 1 --repeats 1 --output runs/piloto_api_1
```

O adaptador usa **Responses API** com saída JSON estruturada (`text.format=json_schema`) e `store=false`. Referência: https://platform.openai.com/docs/api-reference/responses/create . O código não assume nome de modelo ou custo; confirme suporte ao formato na documentação e na sua conta. O ambiente aqui não realizou requisições reais de API.

Após validar o primeiro caso, aumente para `--limit 5 --max-api-calls 25` **somente com autorização consciente do limite e orçamento verificado**. Não inicie a fase principal enquanto o protocolo e a chave não estiverem congelados e revistos.

## Saídas por execução

- `manifest.json`: versão, modo (`mock` ou `openai`), hash SHA-256 dos cenários, quantidade e versão.
- `full_traces_private.jsonl`: contexto da execução, saídas, crítica, revisão, condições e métricas. **Não fornecer ao modelo**.
- `reviewer_masked.jsonl`: versão com rótulos de condição e premissas removidos, mas justificativas podem revelar a condição; revisão humana necessária.
- `metrics.csv`: métricas objetivas sintéticas quando a chave está disponível; sem a chave, os respectivos campos ficam vazios. Não equivale à rubrica ordinal humana.
- `summary.json`: somas/médias de proxies.

## Decisões metodológicas e riscos

1. **Proponente ≠ contestador ≠ avaliador:** proponente e contestador são etapas separadas, mas no modo API usam o **mesmo modelo**. Portanto, não afirmamos independência entre os dois. O avaliador usa regra determinística e chave separada; isso ainda não equivale a avaliação humana independente.
2. **Não há memória persistente implementada:** a “memória” é texto sintético injetado apenas nas condições B e C. Nenhuma preferência pessoal real é coletada.
3. **O gabarito não participa da geração:** somente `evaluation.py` o consulta depois de receber a saída final. A própria regra de pontuação está declarada nos casos públicos (intencionalmente).
4. **O cegamento não é garantido:** campos formais são normalizados e rótulos de condição são retirados da exportação, mas a linguagem pode denunciar a memória ou a contestação.
5. **O experimento principal NÃO está pré-registrado nem congelado:** 30 cenários exigem revisão técnica antes de análise confirmatória.
6. **Não executar ações no ambiente:** o projeto avalia recomendações sintéticas, não agentes com autoridade de escrita.
7. **Estabilidade e custos reais:** somente no modo API se coletam uso de tokens e latência de chamadas; custos monetários dependem do preço de modelo informado externamente. Modelo determinístico não tem latência/token de inferência comparáveis.
8. **Diferença de orçamento de computação:** C faz três chamadas versus uma em A/B. Eventual ganho precisa ser interpretado em conjunto com custo e viés de múltiplas passagens. Não é uma comparação isolada de “contestação”.

## Próxima etapa do Aurora

Validar 5 casos de calibração por revisão técnica e um piloto limitado na API. Só depois decidir se precisamos de um contestador independente por outro modelo, incorporar incerteza e registrar versões em ADRs.

**Não publicar `data/private/answer_key.json` em repositório aberto enquanto os resultados não estiverem congelados.** Considere manter apenas o material público em GitHub.
