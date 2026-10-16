# Evidências de LL-001

## Inventário inicial — 16/10/2026

| Artefato | Disponibilidade | Natureza |
| --- | --- | --- |
| [Relato e trechos transcritos](relato-2026-10-16.md) | Versionado | Fonte secundária: relato do exercício |
| HTML HTTP integral de CSR e SSR | Não incorporado | Evidência primária pendente |
| Screenshots e imagem conceitual mencionada na conversa | Sem arquivo acessível no contexto consultado | Não incorporados |
| Código, configuração, manifestos e lockfiles dos dois projetos | Não incorporados | Reprodução exata pendente |
| Verificação instrumental da hidratação | Não incorporada | Etapa descrita, sem comprovação separada |

Nenhum arquivo HTML ou imagem foi fabricado para preencher essas lacunas. Uma ilustração conceitual, caso adicionada futuramente, deverá ser identificada como ilustração, sem substituir capturas da execução.

## Protocolo para uma nova captura

1. Registrar a data real, sistema, navegador, Node.js, gerenciador, versões das dependências, commit dos projetos e comandos efetivamente executados. Preservar manifestos e lockfiles.
2. Identificar rota, URL local, configuração de renderização e modo de execução: desenvolvimento, build ou servidor de produção. Confirmar SSR habilitado e descartar pré-renderização estática ao investigar SSR por requisição.
3. Salvar a resposta HTML original de cada URL pela aba Network/Response ou cliente HTTP. Não usar apenas o DOM da aba Elements, que pode ter sido modificado pelo JavaScript.
4. Conferir no corpo da resposta o contêiner e a entrada JavaScript do CSR, e o título e texto do SSR. Conservar a resposta integral, respeitando a revisão de dados sensíveis.
5. Se investigar hidratação, registrar separadamente a execução do cliente e a associação de interatividade; HTML com conteúdo, sozinho, não prova hidratação bem-sucedida.
6. Adicionar arquivos em subdiretório com a data real da nova execução e um manifesto com origem, comandos, resultados e hashes SHA-256 dos artefatos. Não atribuir a nova captura a 16/10/2026 se produzida em outra data.
7. Atualizar o inventário, relacionar cada afirmação aos arquivos correspondentes e versionar a alteração. Preservar a distinção entre relato original e reprodução posterior.
