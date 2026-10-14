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

## Etapa 6 — CLI e testes de integração

Adicionada main.py com argparse, ajuda, exemplos, erro em português e código de
saída 2 para argumentos inválidos. A saída de sucesso contém somente a senha.
Adicionados 20 testes reais de subprocesso, cobrindo todos os exemplos pedidos,
limites, seleção única, erros, ajuda e execução a partir de outra pasta.
Executado `.venv\Scripts\python.exe -m pytest -q`: 61 testes aprovados.
Nenhuma senha dos subprocessos foi salva em arquivo ou incluída neste diário.
Preparados iniciar.cmd (sem scripts PowerShell) e workflow Windows/Linux,
Python 3.11/3.12. O workflow ainda não foi executado no GitHub.

## Etapa 7 — documentação e revisão

Criados README, licença MIT, notas da versão e rascunho de fórum. A documentação
explica instalação sem depender de Activate.ps1, seleção das categorias,
códigos de saída e limitações. Consultadas as referências oficiais de secrets
e argparse; confirmado que secrets é adequado para senhas.
A revisão reconhece que o algoritmo não promete distribuição uniforme entre
todas as senhas válidas e que tamanho curto não implica senha forte.
O pedido foi analisado com elementos CO-STAR, sem inventar um prompt enviado.
Teste em Python 3.11.17: 61 aprovados. Em Python 3.12.15: 61 aprovados.
A primeira verificação automatizada de make install falhou: o verificador
estava usando o executável da própria .venv que seria recriada. No Windows,
o executável em uso impede essa operação. A execução direta funcionou; o
verificador foi executado novamente com Python-base, fora do ambiente virtual.
GNU Make 4.4.1 local: make install, make test e make run aprovados.
iniciar.cmd foi executado com tamanho 12, maiúsculas e números: aprovado.
As saídas de senha desses comandos foram capturadas apenas em memória e
omitidas dos relatórios. pip check não encontrou dependências incompatíveis.

## Etapa 8 — preparação da entrega

Preparado o relatório VALIDACAO.md, com resultados locais e pendências externas.
O histórico será encerrado com sete commits e tag local v1.0.0. Uma cópia ZIP
é criada apenas dos arquivos versionados. A publicação e a Release não foram
realizadas: o pedido original exige aprovação do autor antes dessas ações.
O acesso ao GitHub funciona no contexto do Windows, mas falhou no ambiente
isolado; nenhum token foi copiado para o projeto.

## Etapa 9 — publicação aprovada

O autor respondeu “sim” à pergunta específica sobre publicar no GitHub e
criar a Release. Criado o repositório público gerador-senhas-ufg, enviados
os sete commits iniciais e a tag v1.0.0, criada a Release com as notas.
Nenhuma tag foi movida ou histórico reescrito.

Acesso público confirmado com requisições sem credenciais: páginas do
repositório e da Release retornaram sucesso. O HTML do GitHub contém
README renderizado e tabelas.

O workflow executou quatro jobs em Windows/Ubuntu e Python 3.11/3.12;
todos foram aprovados. Evidência: https://github.com/Abimaeltavares/gerador-senhas-ufg/actions/runs/38488310328.
Um oitavo commit atualiza README, validação, diário e postagem com links
e resultados reais. O código executável permanece o mesmo da tag validada.
A submissão no fórum e o comentário em trabalho de colega não foram realizados.
