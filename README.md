# Projeto Aurora

> Investigação experimental sobre arquiteturas de decisão, avaliação, autoridade e execução em sistemas inteligentes.

**Status:** investigação em andamento  
**Versão conceitual:** v0.1  
**Artefato experimental:** Óruias

---

## O que é o Projeto Aurora?

O Projeto Aurora é um campo de investigação em arquitetura de sistemas inteligentes.

Sua questão inicial parte de uma observação simples:

**nem toda decisão de um sistema precisa ser entregue ao mesmo mecanismo — e nem toda decisão precisa ser entregue a um LLM.**

Sistemas contemporâneos baseados em agentes tendem a concentrar diferentes responsabilidades em modelos generalistas: interpretação, planejamento, decisão, avaliação e acionamento de ferramentas.

Aurora investiga uma alternativa arquitetural:

> diferentes classes de problemas podem exigir diferentes mecanismos de decisão, níveis de autonomia, critérios de avaliação e limites de autoridade.

O objetivo não é substituir LLMs, mas investigar **onde cada tipo de inteligência deve residir dentro de uma arquitetura**.

---

## Problema de investigação

Quando um sistema inteligente recebe uma situação do ambiente, surgem questões diferentes que frequentemente são tratadas como uma única "decisão":

1. Como interpretar e classificar a situação?
2. Qual mecanismo deve tratá-la?
3. Qual ação deve ser escolhida?
4. Como avaliar a decisão produzida?
5. O sistema possui autoridade para executá-la?
6. Como executar e observar seus efeitos?

Aurora investiga se essas responsabilidades devem permanecer concentradas em um único agente/modelo ou ser explicitamente separadas pela arquitetura.

---

## Hipótese arquitetural inicial

A decomposição atualmente investigada é:

`ambiente → percepção → interpretação/classificação → meta-decisão → decisão funcional → avaliação → decisão de autoridade → execução → observação/feedback`

### Meta-decisão

Determina **qual mecanismo deve tratar determinada classe de problema**.

Esse mecanismo pode ser, por exemplo:

- regra determinística;
- algoritmo ou modelo especializado;
- mecanismo probabilístico;
- LLM;
- sistema composto;
- humano.

O humano não é necessariamente o último estágio de uma cadeia de fallback. Pode ser o mecanismo deliberadamente selecionado conforme risco, ambiguidade, contexto ou autoridade requerida.

### Decisão funcional

Determina **qual ação ou resposta deve ser produzida** para o problema apresentado.

### Avaliação

Verifica a qualidade, conformidade ou adequação da decisão segundo critérios que não precisam pertencer ao componente que produziu a decisão.

### Decisão de autoridade

Determina **se a ação escolhida pode efetivamente ser executada**, segundo políticas, identidade, contexto, risco e limites previamente estabelecidos.

### Execução

Realiza a ação autorizada no ambiente.

---

## Princípios em investigação

### Autoridade como propriedade arquitetural

> **Autoridade não será um comportamento esperado do agente. Será uma propriedade da arquitetura.**

O sistema não deve depender exclusivamente de um modelo "saber" que determinada ação está fora de sua autoridade.

Os limites devem poder ser representados e aplicados arquiteturalmente.

### Inteligência distribuída

> **Inteligência não precisa estar concentrada em um único modelo.**

Diferentes mecanismos podem apresentar vantagens diferentes conforme a classe de problema.

### Autonomia operacional ≠ autonomia de finalidade

Um sistema pode possuir capacidade operacional para realizar ações sem possuir autoridade irrestrita para determinar seus próprios objetivos ou executá-los.

### Separação de responsabilidades

Uma das hipóteses investigadas é que:

> quem decide não precisa ser quem executa;  
> quem executa não precisa ser quem avalia;  
> quem avalia não precisa definir os critérios de avaliação;  
> quem produz uma decisão não precisa possuir autoridade para executá-la.

Essas separações são hipóteses arquiteturais e deverão ser confrontadas experimentalmente.

---

## Óruias

**Óruias é o primeiro artefato experimental do Projeto Aurora.**

Aurora é o campo de investigação.

Óruias será utilizado para transformar hipóteses conceituais em componentes implementáveis, observáveis e testáveis.

O objetivo do artefato não é demonstrar que as hipóteses do Projeto Aurora estão corretas.

Seu objetivo é permitir que sejam **testadas**.

---

## O que Aurora não reivindica

Este projeto não parte da premissa de que os mecanismos aqui investigados sejam individualmente novos.

Há antecedentes importantes em áreas como:

- algorithm selection;
- expert systems;
- blackboard architectures;
- adaptive control;
- workflow management;
- mixed-initiative systems;
- policy decision/enforcement;
- multi-agent systems;
- autonomic computing;
- neural-symbolic systems;
- mixture of experts;
- model routing;
- LLM agents;
- runtime authorization.

A investigação histórica e bibliográfica faz parte do próprio projeto.

A eventual contribuição de Aurora deverá ser determinada por comparação sistemática com esses antecedentes e por evidência experimental — não por reivindicação prévia de originalidade.

---

## Pergunta de pesquisa atual

A pergunta provisória que orienta esta fase é:

> **Em quais condições a separação entre seleção do mecanismo decisório, decisão funcional, avaliação, autoridade e execução produz vantagens mensuráveis em relação a arquiteturas centradas em um agente ou modelo generalista?**

Essas vantagens poderão envolver:

- previsibilidade;
- segurança;
- auditabilidade;
- custo;
- latência;
- qualidade da decisão;
- redução de chamadas a modelos;
- controle de autoridade;
- intervenção humana;
- complexidade arquitetural.

A própria complexidade introduzida pela decomposição será tratada como custo e variável experimental.

---

## Business-Driven Architecture

A investigação arquitetural não será limitada à viabilidade técnica.

À medida que o projeto evoluir, decisões deverão também ser analisadas considerando:

`problema de negócio → requisitos → capacidades → arquitetura → custo → risco → governança → valor`

Isso inclui requisitos funcionais e não funcionais, TCO, impacto financeiro, risco, governança e capacidade organizacional.

Uma arquitetura tecnicamente superior pode não ser a solução arquitetural adequada para determinado contexto.

---

## Método de investigação

Aurora adota um processo incremental e falsificável:

`literatura → hipótese → arquitetura → experimento → evidência → análise → revisão`

As hipóteses poderão ser confirmadas, limitadas, reformuladas ou descartadas.

Os documentos deste repositório serão versionados para preservar não apenas os resultados, mas também a evolução das decisões arquiteturais.

---

## Estado atual

**Fase: formulação e investigação conceitual.**

Neste momento estão em desenvolvimento:

- delimitação do problema;
- genealogia histórica das arquiteturas relacionadas;
- revisão bibliográfica;
- taxonomia das diferentes formas de decisão;
- definição dos limites entre decisão, avaliação, autoridade e execução;
- definição dos requisitos do primeiro artefato experimental;
- critérios e métricas para futuros experimentos.

Nenhuma arquitetura publicada nesta fase deve ser interpretada como solução definitiva.

---

## Estrutura prevista do repositório

    projeto-aurora/
    │
    ├── README.md
    ├── docs/
    │   ├── problema-de-investigacao.md
    │   ├── principios-e-hipoteses.md
    │   └── arquitetura-conceitual.md
    │
    ├── research/
    │   ├── referencias.md
    │   └── research-log.md
    │
    ├── oruias/
    │   └── README.md
    │
    └── CHANGELOG.md

---

## Research Log

O desenvolvimento do Projeto Aurora será registrado progressivamente.

Cada entrada poderá conter:

`fonte → conceito → interpretação → relação com Aurora → hipótese → evidência necessária → resultado`

As referências poderão assumir diferentes estados:

- **DISCIPLINA** — material proveniente da formação acadêmica;
- **EM LEITURA** — fonte atualmente em análise;
- **INCORPORADA** — conceito utilizado na investigação;
- **CITADA** — referência formalmente utilizada em publicação ou documento;
- **CONTESTADA** — fonte ou proposição confrontada por outra evidência.

---

## Autoria

**Isis Fantini Carneiro Klein**

Profissional de Tecnologia da Informação e pesquisadora independente em arquitetura de sistemas inteligentes.

Projeto desenvolvido em diálogo com estudos em Arquitetura de Soluções Digitais e investigação independente sobre sistemas de decisão, arquiteturas híbridas, IA e governança.

---

## Nota metodológica

Este repositório documenta uma investigação em andamento.

**Publicável não significa concluído. Significa rastreável.**

Hipóteses, modelos e diagramas poderão mudar conforme novas referências, implementações e evidências forem incorporadas ao projeto.
