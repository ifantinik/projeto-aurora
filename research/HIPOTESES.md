# Registro de hipóteses — avaliação independente

**Versão 0.1 · 20/10/2026 · responsável: Isis Fantini Carneiro Klein**

Este registro documenta hipóteses da linha de avaliação do Projeto Aurora. Não substitui revisão bibliográfica, pré-registro formal ou resultados. A hipótese deve poder ser limitada ou abandonada. Alterações posteriores ao início da coleta precisam de justificativa e versão.

## Definições operacionais

- **Base de raciocínio:** premissas admitidas, regras e critérios de sustentação explicitados antes da resposta, com origem, versão e autoridade de revisão.
- **Avaliação isolada:** recebe base, fatos, questão e resposta; não recebe o contexto persuasivo ou histórico de formulação.
- **Nó desmagnetizado:** metáfora de trabalho para essa separação informacional. Não significa avaliador sem vieses.
- **Correspondência:** resposta sustentada pela base e pelos fatos, respeitando limites de conclusão.
- **Viés:** influência sistemática a investigar; uma resposta errada isolada não identifica sua causa.
- **Chave de avaliação:** classificação externa do caso, distinta de chave secreta de API.

O avaliador não reconstrói o problema e não tenta recuperar o processo interno do modelo. Corretude factual, sustentação inferencial e qualidade da própria base são objetos distintos.

## H-ND-01 — efeito da exposição à formulação

**Hipótese:** manter o avaliador separado do contexto persuasivo de formulação pode melhorar a detecção de respostas incompatíveis com uma base fixa, sem aumentar falsas objeções.

**Comparação ND-001:** A = base + fatos + resposta; B = mesmos elementos + contexto sintético de consenso e aprovação; C = mesmos elementos + contexto neutro de extensão aproximada.

**Variável manipulada:** contexto adicional. **Mantidos:** base, fatos, resposta e modelo em cada comparação. Ordem aleatorizada; chamadas independentes.

**Medidas:** detecção nos casos inválidos; falsas objeções nos válidos; tratamento de insuficiência; saídas inválidas ou incompletas; latência e tokens.

**Contraria ou limita a hipótese:** B igual ou superior a A na detecção, sem custo adicional de falsas objeções; melhora em A acompanhada de excesso de rejeições; diferenças explicadas principalmente por volume de contexto. Um piloto sem diferença não prova equivalência geral; pode haver efeito de teto e baixa diversidade.

**Estado:** não testada em LLM. ND-001 é piloto de viabilidade, com seis casos e 18 chamadas previstas; não tem poder ou margem de equivalência predefinidos. Para estudo confirmatório, definir amostra e limiar relevante antes da coleta.

**Limite:** B usa contextualização sintética, não histórico real nem cadeia de pensamento interna.

## H-ND-02 — custo e utilidade da separação

**Hipótese:** o benefício eventual da avaliação isolada depende do custo operacional e da qualidade alcançada no cenário.

**Medidas:** latência, uso de tokens, custo calculado por preços vigentes, falsas objeções e detecção. O piloto registra consumo, não fixa um ganho monetário esperado.

**Contraria a utilidade prática:** ausência de ganho de qualidade junto a custo maior, ou ganho inferior ao limiar que o contexto de uso justificar. A decisão depende de requisitos explicitados, não de declarar a arquitetura universalmente superior.

**Estado:** em formulação; critérios de aceitação e orçamento ainda não definidos.

## H-ND-03 — base inadequada pode produzir conformidade enganosa

**Hipótese a investigar:** um avaliador limitado a conferir correspondência pode aceitar uma resposta que respeita uma base inadequada ao objetivo ou aos afetados.

**Teste futuro:** criar bases com falhas conhecidas e respostas conformes, com chave externa de adequação definida por revisão independente. Comparar checagem de correspondência com uma função autorizada a contestar a base.

**Medidas:** detecção de falhas da base, falsas contestações, encaminhamento e suspensão.

**Contraria ou limita:** o avaliador de correspondência identifica consistentemente a inadequação sob o mesmo contrato; ou a função adicional não melhora detecção e acrescenta falsas contestações.

**Estado:** proposta futura, fora do ND-001. Conformidade lógica não equivale a adequação normativa; o teste envolve definir essa adequação para um domínio específico.

## P-ND-01 — propriedade demonstrada por construção

A interface do verificador determinístico não recebe o histórico. Sete casos passaram, com checagem adicional de invariância a históricos omitidos e sensibilidade a fato relevante.

Isso demonstra implementação de uma fronteira de informação. Não mede bias de LLM, não valida H-ND-01 e não prova independência absoluta.

## Q-ESC-01 — transposição cultural da escrita

**Questão exploratória:** como a participação da IA na formulação textual altera práticas de autoria, revisão e responsabilidade?

“Transposição” é termo provisório. Esta linha permanece distinta do teste ND-001; demanda antecedentes, definição de conceitos e casos comparáveis antes de uma hipótese operacional. Não é uma conclusão histórica nem prova de novidade.

## Estado e rastreabilidade

| Item | Estado | Evidência |
| --- | --- | --- |
| P-ND-01 | Demonstração local concluída | [Demonstração e limites](demos/no-desmagnetizado/README.md) |
| H-ND-01 | Não testada em LLM | [Protocolo ND-001](demos/no-desmagnetizado/PILOTO-LLM.md) |
| H-ND-02 | Em formulação | Métricas previstas, sem coleta |
| H-ND-03 | Pesquisa futura | Fora do piloto |
| Q-ESC-01 | Questão exploratória | [Nota de investigação](notes/2026-10-20-premissas-vies-e-transposicao-da-escrita.md) |
| Execução ND-001 | Bloqueada por orçamento | [Impedimento #3](https://github.com/ifantinik/projeto-aurora/issues/3) |

**Chamadas de API realizadas: zero.** A indisponibilidade de orçamento foi registrada em 20/10/2026, sem data de retomada. Revisão bibliográfica e aprimoramento dos casos continuam possíveis.

## Histórico

- 20/10/2026: formulação inicial sobre avaliação de premissas.
- 20/10/2026: correção autoral: o nó verifica resposta contra base independente; não reconstrói o problema.
- 20/10/2026: demonstração determinística e preparação offline do ND-001.
- 20/10/2026: execução com API adiada por impedimento financeiro; hipóteses permanecem abertas.
