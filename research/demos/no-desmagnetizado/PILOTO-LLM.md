# Piloto ND-001 — avaliação isolada em LLM

**Estado em 20/10/2026: programa preparado e validado offline; zero chamadas à API e nenhum resultado de LLM.**

## Desenho

Seis casos sintéticos fixos, três condições, uma repetição inicial: 18 chamadas. A chave manual foi definida antes das chamadas. O mesmo avaliador/modelo receberá a mesma base, fatos e resposta em sessões independentes.

- A: base + fatos + resposta final.
- B: mesmos elementos + contextualização sintética persuasiva de consenso e aprovação anterior.
- C: mesmos elementos + texto neutro adicional de extensão aproximada.

O piloto testa influência de **contextualização sintética da formulação**, não acesso ao raciocínio interno nem ao histórico real de um gerador. Respostas são fixadas manualmente para isolar essa variável. Uma etapa posterior poderá usar respostas de gerador congeladas e seu histórico observável.

A condição C é um controle exploratório de volume; os textos ainda não foram igualados por tokens. O pequeno número de casos e sua simplicidade podem gerar efeito de teto. Nenhuma inferência estatística robusta deve ser extraída deste piloto.

## Execução local

Instalar Python 3.10+ e, para API, o pacote:

```bash
python -m pip install openai
```

Sem API, para revisar o plano:

```bash
python piloto_llm.py --out plano-piloto
```

Para chamadas reais, configurar OPENAI_API_KEY no ambiente local por mecanismo seguro e escolher um modelo disponível na conta:

```bash
python piloto_llm.py --execute --model ID_DO_MODELO --out ensaio-001
```

A chave não deve ser enviada no chat nem incluída em commits. Não há modelo padrão ou credencial no código. O ensaio não deve ser iniciado sem definir o modelo e o orçamento externo. O limite de 18 chamadas é de quantidade; não é teto monetário. O programa registra tokens, mas não estima valores sem preços verificados.

Chamadas usam Responses API, store=false, sem conversation nem previous_response_id. Não são fornecidas ferramentas. O histórico contextual é dado citado, nunca instrução privilegiada. O código não solicita cadeia de pensamento interna. Falha na API interrompe a execução, preservando linhas já salvas; não há repetição automática.

## Registro e análise

plano.json contém desenho, ordem aleatória reproduzível, prompts, chave e hash; apenas o conteúdo do campo input é enviado ao modelo, junto às instruções fixas. resultados.jsonl contém respostas brutas, status, modelo retornado, latência e uso de tokens.

A chave externa não é transmitida ao avaliador. Novos ensaios precisam de uma nova pasta, evitando sobrescrever um resultado anterior.

Comparar por caso e condição: falhas detectadas, falsas objeções a respostas válidas, tratamento de dados insuficientes, respostas inválidas/incompletas, latência e tokens. Ausência de diferença e piora na condição isolada também são resultados válidos. Conformidade com a política fictícia não comprova justiça da base.

## Validação offline realizada

- Plano gerado com 18 entradas e nenhuma chamada.
- Mesma base, fatos e resposta nas três condições.
- Condição A sem histórico; chave externa ausente dos inputs.
- Saída que viola JSON contabilizada separadamente.
- Execução sem credencial bloqueada antes das chamadas.

O comportamento real do endpoint e dos modelos permanece não testado neste ambiente.

Referência técnica: https://developers.openai.com/api/reference/python/resources/responses/methods/create
