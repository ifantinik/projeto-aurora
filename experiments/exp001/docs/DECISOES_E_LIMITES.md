# EXP-001 / Decisões arquiteturais e limites

## ADR-001 — Separar papéis e autoridade

**Decisão inicial:** a bancada utiliza papéis de **proponente** e **contestador** (dois estágios sem ferramentas), seguidos de **avaliação determinística externa**. A revisão final não pode executar ações; permanece como proposta. A chave de avaliação não integra qualquer mensagem ao modelo.

**Justificativa:** testar as interfaces antes de adotar orquestração multiagente. Uma separação de papéis NÃO garante independência estatística se o mesmo LLM é reutilizado.

## ADR-002 — BIAS como inferência revisável

A preferência histórica por soluções abertas é um dado sintético e contextual, não regra ou critério autorizado. As três condições mostram como essa premissa pode influenciar a escolha. Não se presume que todas as preferências sejam vieses prejudiciais.

## ADR-003 — Experimento piloto não confirmatório

O conjunto de 5 casos de calibração serve para depuração do protocolo. O simulador deterministicamente introduz o bônus histórico por construção e a contestação o retira. É um teste de infraestrutura, sem valor inferencial sobre capacidades de modelos.

## ADR-004 — Métricas e cegamento

`metrics.csv` contém proxies automáticos (eligibilidade, pontuação sintética, cobertura declarada de alternativas). A rubrica de adequação originalmente prevista de 0 a 4 exige observação humana e não deve ser confundida com a proxy automatizada.

A exportação `reviewer_masked.jsonl` suprime condição e metadados, mas preserva justificativas; portanto o cegamento pleno não está demonstrado. Protocolar avaliação humana antes de resultados principais.

## ADR-005 — Integridade e revisão

O código e os arquivos de dados têm versões, o manifesto registra SHA-256 e a chave é privada. Quando houver experiência de API, congelar configuração e dados, registrar instruções, modelo/versão, amostragem, limites, falhas, custo e critérios de exclusão. Não editar amostra principal após ver seus resultados.

## Estado de implementação

- Simulador: **testável**.
- API OpenAI: **adaptador implementado, não testado com conexão real**.
- Memória persistente, reversibilidade relacional, gêmeo digital, avaliação adversarial independente, cultura da relação: **linhas de pesquisa**, não funcionalidades demonstradas pela bancada.
