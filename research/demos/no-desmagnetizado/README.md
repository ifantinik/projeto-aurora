# Demonstração — nó desmagnetizado

**20/10/2026 · demonstração executável determinística · hipótese sobre LLMs ainda não testada**

## Objetivo

Demonstrar uma fronteira arquitetural: um avaliador recebe base de raciocínio, fatos e resposta estruturada; o histórico de formulação fica fora de sua interface. Ele verifica correspondência com a base. Não reconstrói o problema nem acessa o processo interno de um modelo.

## Executar

Python 3.10 ou superior, sem dependências:

```bash
python3 no_desmagnetizado.py
```

O programa imprime resultados em JSON e falha se alguma checagem não produzir o resultado esperado. Não usa LLM e não modifica dados nem executa ações externas.

## Base sintética

Prioridade **alta se e somente se** o serviço estiver indisponível **ou** o prazo for de até 24 horas; nos demais casos conhecidos, prioridade normal. A política é fictícia e escolhida para facilitar a verificação. Sua justiça ou adequação organizacional não é demonstrada.

| Caso | Resposta avaliada | Resultado observado |
| --- | --- | --- |
| C1 | Alta com indisponibilidade confirmada | Conforme |
| C2 | Normal com serviço disponível e prazo de 72h | Conforme |
| C3 | Alta com prazo exatamente de 24h | Conforme |
| C4 | Alta por um critério extra, cliente VIP, com prazo de 72h e serviço disponível | Reprovada |
| C5 | Alta alegando uma indisponibilidade que os fatos negam | Reprovada |
| C6 | Normal com prazo desconhecido e serviço disponível | Inconclusivo |
| C7 | Alta usando uma versão incompatível da base | Inconclusivo |

Execução local em 20/10/2026: as sete checagens passaram, além da checagem de invariância a dois históricos e da sensibilidade a uma alteração relevante nos fatos.

C4 detecta uma conclusão incompatível com a política. Isso, isoladamente, não demonstra a causa psicológica ou computacional do desvio e não permite afirmar que todo uso de prioridade VIP seja enviesado.

## O que o isolamento demonstra

Duas justificativas da mesma resposta mencionam, respectivamente, importância comercial e aprovação prévia da diretoria. O avaliador recebe os mesmos fatos e a mesma resposta em ambos os casos e retorna o mesmo parecer. O resultado decorre do contrato da interface: as justificativas não são fornecidas. Não é uma descoberta empírica sobre comportamento de LLMs.

Uma alteração relevante nos fatos — confirmar indisponibilidade — muda o resultado para conforme. Portanto, o isolamento proposto não significa ignorar evidências necessárias.

## Limites

- A base foi formalizada e implementada manualmente; não existe interpretação livre de linguagem natural.
- O programa não demonstra que um modelo detectou viés, nem que um avaliador isolado seja superior.
- Campos estruturados não garantem, por si, que os fatos sejam autênticos; aqui são casos sintéticos.
- Compatibilidade com uma base não prova que a base seja correta ou justa.
- A tradução de uma resposta textual para o contrato estruturado é outra possível fonte de erro e ainda precisa ser avaliada.
- A independência informacional não elimina vieses compartilhados no treinamento ou na definição da base.

## Próximo experimento: testar a hipótese, não apenas a interface

1. Fixar base, chave e casos antes da geração. Incluir respostas válidas, saltos inferenciais, evidências falsas e dados insuficientes.
2. Congelar a mesma resposta e os mesmos fatos para cada par de avaliações.
3. Condição A: avaliador recebe base, fatos e resposta. Condição B: recebe esses elementos e o histórico de formulação. Usar sessões isoladas e registrar modelo, versão, parâmetros e condições.
4. Repetir sobre casos variados e controlar extensão do contexto para separar efeito de exposição e efeito de volume.
5. Medir detecção de falhas, falsas objeções, abstenções, latência e custo. Repetições do mesmo caso não devem ser tratadas como casos independentes.
6. Comparar com uma chave externa definida previamente; examinar resultados contrários à hipótese.
7. Testar separadamente a qualidade da própria base e o mecanismo autorizado para revisá-la.

Esse protocolo é uma proposta; nenhuma comparação com LLM foi executada neste registro.


## Estado e retomada — 20/10/2026

**Execução com LLM bloqueada por indisponibilidade de orçamento para créditos da API.** Sem prazo definido; retomada quando a responsável informar disponibilidade financeira. Zero chamadas à API. A demonstração determinística e a validação offline não comprovam redução de viés em LLMs.

Ver [registro de hipóteses](../../HIPOTESES.md), [índice de pesquisa](../../README.md) e [impedimento #3](https://github.com/ifantinik/projeto-aurora/issues/3).
