# LL-001 — CSR em React + Vite × SSR em Nuxt

**Data do exercício:** 16/10/2026

**Data do registro:** 16/10/2026

**Natureza:** exercício de aprendizagem em Arquitetura de Soluções Digitais

**Estado:** documentação de observações relatadas; sem reexecução ou capturas primárias incorporadas nesta publicação.

> Este teste pertence ao learning lab. Não valida hipóteses do Projeto Aurora e não integra a evidência experimental de seu núcleo.

## Questão

Onde ocorre a renderização inicial do conteúdo da página e o que o HTML recebido permite observar sobre essa responsabilidade?

## Hipótese / expectativa didática

No caso configurado como CSR, espera-se receber uma estrutura HTML sem o conteúdo da aplicação, que será produzido pelo React no navegador após carregar o JavaScript. No caso configurado como SSR, espera-se receber HTML com conteúdo produzido no servidor; o cliente poderá então hidratar esse HTML para associar o comportamento interativo.

A expectativa diz respeito às configurações observadas, não a uma propriedade obrigatória dos frameworks: React pode participar de SSR e Nuxt admite diferentes estratégias de renderização.

## Casos e ambiente conhecido

| Aspecto | CSR | SSR |
| --- | --- | --- |
| Projeto local relatado | `portfolio-spa` | `portfolio-ssr-poc` |
| Tecnologia | React + Vite | Nuxt |
| Versão informada | Vite v8.3.4 | Nuxt 4.6.1 |
| HTML inicial relatado | `<div id="root"></div>` e referência a `/src/main.jsx` | `<h1>Projetos</h1>` e texto da página |
| Etapa posterior | Execução do JavaScript e renderização no cliente | Hidratação no cliente |

Versões transcritas do relato fornecido, sem conferência de manifesto ou lockfile. Versões de React, Node.js, gerenciador de pacotes, navegador e sistema operacional da execução não foram registradas. Código, configurações, rotas, portas e comandos exatos também não estão disponíveis neste registro.

## Procedimento relatado

1. Utilizar duas aplicações mínimas: `portfolio-spa` para CSR e `portfolio-ssr-poc` para SSR.
2. Consultar o HTML recebido pelo navegador em cada aplicação, procurando o conteúdo da página antes da execução do JavaScript do cliente.
3. Comparar o contêiner vazio e a entrada JavaScript do caso CSR com o título e o texto já presentes no caso SSR.
4. Interpretar a diferença em termos de responsabilidade pela renderização inicial.

O relato não identifica a ferramenta de inspeção utilizada nem demonstra uma medição instrumental da hidratação. Esta publicação documenta o exercício anterior; não afirma tê-lo executado novamente.

## Observações e evidências disponíveis

- **O-01 — CSR:** o relato indica um contêiner `root` vazio e referência a `/src/main.jsx` no HTML inicial. O conteúdo da interface seria produzido no cliente.
- **O-02 — SSR:** o relato indica `<h1>Projetos</h1>` e texto da página no HTML recebido. O texto integral não foi fornecido e não foi reconstruído.
- **O-03 — Hidratação:** descrita no relato como etapa posterior do Nuxt; não há captura de eventos, logs ou teste de interatividade que a comprove separadamente.

As transcrições e sua proveniência estão em [relato de 16/10/2026](evidencias/relato-2026-10-16.md). O [inventário de evidências](evidencias/README.md) distingue o que está disponível do que permanece ausente. Não há screenshots, respostas HTTP completas ou implementações mínimas anexadas.

## Conclusão

As observações relatadas são compatíveis com a expectativa: no caso CSR o navegador assume a produção inicial do conteúdo da aplicação; no caso SSR o conteúdo já está no HTML entregue pelo servidor. A aparência final pode ser semelhante, embora a responsabilidade pela renderização inicial esteja distribuída de forma diferente.

A presença de conteúdo no HTML, isoladamente, não distingue SSR por requisição de HTML pré-renderizado estaticamente. A classificação SSR deste exercício depende também da configuração Nuxt relatada, ainda não disponibilizada. A hidratação é uma etapa distinta da geração inicial de HTML e não foi verificada instrumentalmente neste registro.

## Limitações

- Registro baseado em relato, sem artefatos primários que permitam auditoria independente da execução original.
- Sem código e lockfiles versionados, a reprodução exata não está garantida.
- Comparação entre implementações e frameworks diferentes; não isola a estratégia de renderização como única variável.
- Sem controle documentado de cache, rede, build, conteúdo equivalente ou modo de execução. A referência `/src/main.jsx` não deve ser generalizada para o HTML de produção do Vite.
- Sem métricas de desempenho, SEO, acessibilidade, custo, escalabilidade ou experiência do usuário. Não se conclui superioridade de uma abordagem.
- Nenhuma hipótese sobre mecanismos decisórios, avaliação ou autoridade do Aurora foi submetida a teste.

## Relação com Arquitetura de Soluções Digitais

O exercício treina a identificação de responsabilidades e fronteiras entre cliente e servidor a partir de um artefato observável: o HTML recebido. Essa leitura ajuda a formular perguntas sobre requisitos de conteúdo inicial, interatividade, infraestrutura e operação. Os impactos sobre desempenho, indexação e custo exigem investigação própria e métricas adequadas ao contexto de negócio.

Trata-se de formação de repertório arquitetural. Uma analogia sobre distribuição de responsabilidades não transfere resultados para as hipóteses do Projeto Aurora.

## Continuidade e versionamento

As [decisões do registro](decisoes.md) preservam os critérios adotados. Para uma nova execução, seguir o [protocolo de captura](evidencias/README.md#protocolo-para-uma-nova-captura), anexar artefatos reais com nova data e atualizar as conclusões conforme a força das evidências. O histórico Git registra a evolução documental; não substitui o histórico de execução.
