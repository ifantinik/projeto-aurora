# Decisões de documentação — LL-001

## D-001 — Separar aprendizagem e validação do Aurora

**Data:** 16/10/2026

**Estado:** adotada

**Contexto:** o exercício nasceu da formação em Arquitetura de Soluções Digitais; seu objeto é renderização inicial em aplicações web. O núcleo Aurora investiga arquiteturas de decisão, avaliação, autoridade e execução.

**Decisão:** publicar em `learning-lab/frontend/csr-vs-ssr`, com identificador LL-001 e aviso explícito de escopo. Não registrar o resultado como validação experimental das hipóteses do núcleo.

**Consequência:** o repositório compartilha repertório formativo sem confundir objetos e critérios de investigação. Uma aplicação futura ao Aurora exigirá protocolo próprio.

## D-002 — Publicar o relato com lacunas explícitas

**Data:** 16/10/2026

**Estado:** adotada

**Contexto:** há trechos e versões informados, mas não há respostas HTTP completas, imagens acessíveis, código ou lockfiles incorporados.

**Decisão:** preservar as transcrições em arquivo Markdown identificado como relato. Não criar screenshots, HTML integral, comandos históricos ou resultados de medição fictícios. Tratar hidratação como etapa descrita sem verificação instrumental separada.

**Consequência:** o registro é público e versionado, mas sua auditabilidade e reprodução permanecem limitadas. Capturas posteriores receberão sua data real e proveniência.

## D-003 — Restringir a conclusão à responsabilidade de renderização

**Data:** 16/10/2026

**Estado:** adotada

**Contexto:** as observações tratam do conteúdo do HTML inicial; não há métricas ou isolamento de variáveis entre frameworks.

**Decisão:** registrar compatibilidade com a expectativa didática, sem concluir superioridade, ganhos de desempenho ou SEO. Explicitar que HTML com conteúdo também pode resultar de pré-renderização estática.

**Consequência:** novos estudos devem controlar ambiente, estratégia e métricas antes de sustentar recomendações arquiteturais.

## Histórico

Alterações de escopo ou método devem acrescentar uma decisão datada, referenciar a anterior e atualizar seu estado quando substituída. O histórico Git preserva versões e autoria dos documentos; datas de execução devem ser registradas separadamente.
