# Diário de desenvolvimento

Data da sessão: 13 de outubro de 2026 (America/Sao_Paulo).

## Pedido e participação humana

O autor forneceu um texto detalhado definindo o Gerador de Senhas Seguras:
Python 3.11+, CLI, argparse/secrets/string, pytest e requisitos RF01–RF13.
O texto também pediu documentação verdadeira, commits reais e aprovação
antes da publicação no GitHub ou criação de release.

Trechos literais dos pedidos do autor:
- “Comece agora pela ETAPA 1: analisar o ambiente, apresentar o plano de desenvolvimento e definir a arquitetura mínima. Não implemente ainda o código principal. Aguarde minha aprovação para continuar.”
- Após a inspeção e o plano: “vc cria e faz tudo que precisa ai”.

O segundo pedido autorizou a execução das etapas locais. A aprovação específica
de publicação será solicitada com o projeto pronto. Não se declara revisão humana
do código nem ganhos de produtividade que não foram medidos.

## Etapa 1 — inspeção

A pasta disponível nesta sessão estava vazia. Git, GitHub CLI e VS Code foram
encontrados; Python não estava no PATH nem nos locais verificados.
A autenticação do GitHub falhou no ambiente isolado.
O PowerShell disponível era 7.6.6, com política RemoteSigned.
Nenhum arquivo foi alterado nessa etapa.

## Etapa 2 — preparação

Criada uma subpasta gerador-senhas-ufg. Python é preparado localmente em .tools,
com uv, sem exigir mudança da política de scripts nem instalação global.
Criados escopo, arquitetura mínima, instruções do agente e exclusões do Git.
A IA elaborou esses arquivos a partir do pedido; o autor escolheu o projeto e
autorizou a execução. Resultados de testes serão registrados após sua execução.

## Etapa 3 — TDD Red do núcleo

Escritos 41 casos de teste antes da implementação. O núcleo inicial declarava
apenas o contrato e levantava NotImplementedError. Executado:
`.venv\Scripts\python.exe -m pytest -q`.
Resultado real: 41 falhas. As falhas eram esperadas: ausência de implementação
e ausência de secrets no módulo ainda vazio. Não se confundiram com aprovação.
Os testes verificam as 16 combinações de seleção, limites, erros, variação
observada e chamadas a secrets.choice/secrets.randbelow.

## Etapa 4 — TDD Green do núcleo

Implementados seleção de categorias, validação de tamanho, preenchimento com
secrets.choice e Fisher–Yates com secrets.randbelow. Mesmo comando anterior:
41 testes aprovados em execução real. O núcleo não imprime nem salva senhas.
A revisão do código confirmou ausência de random comum e uso exclusivo de
secrets para escolhas de caracteres e índices aleatórios.

## Etapa 5 — Refactor do núcleo

Extraído o Fisher–Yates para _embaralhar, com responsabilidade e docstring
próprias. Os 41 testes existentes passaram novamente, sem mudança de contrato.
O ciclo Red → Green → Refactor foi observado no núcleo; não se afirma que
cada arquivo ou teste posterior foi produzido por TDD.
