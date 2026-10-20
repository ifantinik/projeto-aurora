# Nota de investigação 001 — premissas, viés e transposição cultural da escrita

**Projeto Aurora / Óruias · 20/10/2026 · estado: questões e hipóteses, sem resultado experimental**

Esta nota reúne duas perguntas surgidas da investigação. Elas se relacionam pela circulação de linguagem e critérios entre pessoas e sistemas, mas devem ser estudadas separadamente. O texto registra formulações de trabalho; não reivindica originalidade, causalidade demonstrada nem uma implementação concluída.

## 1. Avaliação de premissas em decisões assistidas por IA

Verificar se os dados citados são corretos não equivale a avaliar se a decisão está sustentada. Dados corretos podem compor uma conclusão inadequada quando o problema foi enquadrado de forma estreita, as evidências foram selecionadas de maneira enviesada, uma premissa é inválida ou a inferência ultrapassa o que os dados permitem.

A avaliação precisa distinguir pelo menos três níveis:

| Nível | Pergunta |
| --- | --- |
| Informação | Qual é a origem, qualidade, contexto e suficiência das evidências? |
| Justificação | Quais premissas e critérios ligam a evidência à conclusão? Que alternativas foram consideradas? |
| Condições da avaliação | Quem definiu a pergunta e os critérios? Que dados, incentivos e dependências são compartilhados? Quem pode contestar, revisar ou suspender? |

Informação inventada, inferência sem sustentação e viés podem coexistir, mas não são a mesma falha. Também não basta separar formalmente o proponente e o avaliador: pessoas ou modelos diferentes podem trabalhar dentro do mesmo enquadramento e reproduzir o mesmo ponto cego. Uma revisão humana registrada é um evento verificável; sua qualidade exige exame próprio.

### Hipótese do nó desmagnetizado

“Nó desmagnetizado” é a metáfora para um avaliador que recebe uma **base de raciocínio estabelecida independentemente da formulação da resposta** e verifica se a resposta corresponde a ela. O nó não reconstrói o problema nem tenta adivinhar o processo interno do modelo. Sua tarefa é examinar a sustentação da resposta segundo essa base.

A base pode explicitar premissas admitidas, critérios, regras de inferência, evidências exigidas, limites de conclusão e condições de escalonamento. Ela precisa ter origem e versão registradas, bem como autoridade definida para sua revisão. O avaliador recebe a base, a questão, a resposta final e evidências consultáveis; na condição de avaliação isolada, não recebe a sequência de prompts, rascunhos, justificativas persuasivas ou avaliações prévias que conduziram à resposta. Esse isolamento é uma proposta experimental, não uma garantia de neutralidade.

O avaliador pode apontar: conclusão incompatível com a base; premissa necessária ausente; evidência insuficiente; aplicação indevida de critério; ou conclusão que excede o alcance autorizado. Se a própria base tiver um viés, a conformidade da resposta com ela não demonstra qualidade da decisão. A contestação da base exige uma função de governança distinta, capaz de suspender a execução e encaminhar a revisão a quem possui autoridade para alterá-la.

**Hipótese experimental:** um avaliador isolado do processo de formulação da resposta pode detectar mais falhas de sustentação do que um avaliador exposto a esse processo, usando a mesma base de raciocínio. Comparar detecção, falsas objeções, custo e tempo. Maior divergência não será tomada automaticamente como maior qualidade. Uma explicação gerada pelo modelo pode ser avaliada como justificação apresentada; ela não será tratada como relato fiel de seu processo interno.

### Cenário a especificar

Construir casos com dados factualmente corretos e respostas que variem entre: sustentação válida, salto inferencial, premissa ausente e aplicação indevida de um critério. Definir e versionar a base e a chave de avaliação antes de gerar as respostas. Comparar: (A) avaliador com acesso à base e à resposta final; (B) avaliador com os mesmos elementos mais o histórico de formulação. Manter casos e base iguais entre condições e registrar detecção, falsas objeções, custo, tempo e divergências. Em um teste separado, inserir um viés na própria base para verificar se o mecanismo de governança o detecta; isso não é função da simples checagem de correspondência.

Esse desenho ainda precisa de controles para diferenças entre avaliadores e de exemplos que possam refutar a hipótese. Ele não constitui experimento realizado.

## 2. Transposição cultural da escrita para a IA

A outra linha investiga uma mudança nas condições de produção e atribuição da escrita. A escrita manual, a máquina de escrever e o computador já alteraram ritmo, revisão, circulação e autoria prática. Com a IA generativa, um sistema também pode propor frases, estruturas, argumentos e respostas no processo de expressão.

**Pergunta:** o que muda quando a formulação que antes passava principalmente pela mão e pela edição da pessoa passa por uma interação com um sistema que produz linguagem? Que competências são deslocadas para formular a pergunta, reconhecer uma contribuição, verificar fatos, examinar premissas, selecionar, recusar e assumir a autoria da versão publicada?

“Transposição” é aqui um nome provisório para essa passagem de práticas e responsabilidades entre meios. Não afirma que as etapas históricas tenham ocorrido uniformemente, que a IA substitua a pessoa, nem que toda escrita assistida constitua uma nova cultura por si só. A formulação autoral “uma escrita sai de um debate” pode orientar a investigação, mas requer casos e comparação para ganhar precisão analítica.

### Ligação com a arquitetura de decisão

Quando um texto da IA entra em uma proposta, relatório ou decisão, sua fluência pode conferir aparência de solidez a um enquadramento já enviesado. O circuito pode atravessar gestor, modelo, equipe e aprovação institucional sem que ninguém tenha condições reais de questionar a premissa inicial. Essa é uma possibilidade arquitetural a examinar, não uma propriedade inevitável da IA ou das organizações.

O vínculo entre as duas linhas é a necessidade de preservar rastreabilidade e contestação: qual parte foi observada, inferida, proposta, revisada e assumida por quem? Uma resposta fluente não garante correção; uma explicação convincente não demonstra como o modelo chegou ao resultado.

## Próximos registros

1. Delimitar conceitos de viés, falha factual, erro de inferência e enquadramento, buscando antecedentes bibliográficos.
2. Especificar a base de raciocínio, casos controlados e chave de avaliação para testar a correspondência da resposta sem expor o avaliador ao processo de formulação.
3. Reunir exemplos comparáveis da produção textual em diferentes meios, sem pressupor uma narrativa histórica linear.
4. Registrar quando uma evidência altera, limita ou refuta cada hipótese.
5. Decidir separadamente se cada linha cabe no recorte do TCC ou permanece na investigação pessoal do Aurora.

**Critério de publicação:** este registro torna perguntas e método proposto inspecionáveis. O próximo avanço depende de referências verificadas e evidência experimental.
