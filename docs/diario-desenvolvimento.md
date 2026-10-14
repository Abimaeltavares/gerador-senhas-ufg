# Diário de desenvolvimento

Data da sessão: 13 de outubro de 2026 (America/Sao_Paulo).

## Pedido e participação humana

O autor forneceu um texto detalhado definindo o Gerador de Senhas Seguras:
Python 3.11+, CLI, argparse/secrets/string, pytest e requisitos RF01–RF13.
O texto também pediu documentação verdadeira, commits reais e aprovação
antes da publicação no GitHub ou criação de release.

Trechos literais dos pedidos do autor:
- “Comece agora pela ETAPA 1: analisar o ambiente, apresentar o plano de desenvolvimento e definir a arquitetura mínima. Não implemente ainda o código principal. Aguarde minha aprovação para continuar.”

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

Criados README, licença MIT e notas da versão. A documentação
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
Um oitavo commit atualiza README, validação e diário com links
e resultados reais. O código executável permanece o mesmo da tag validada.

## Etapa 10 — sincronização dos artefatos de entrega

Em 14 de outubro de 2026, o autor solicitou atualizar os documentos antigos
ainda presentes nos downloads da versão. A tag v1.0.0 e o pacote ZIP da
Release foram sincronizados com a documentação atual. O código executável
e os testes não foram alterados. O histórico de commits foi preservado.
A listagem do pacote e a referência remota da tag são conferidas após a atualização.

## Etapa 11 — complementação da validação e documentação

Em 14 de outubro de 2026, após analisar as imagens do curso, o autor pediu
“quais alterações precisa fazer ?” e autorizou o plano com “bora fazer”.
Foram adicionados Ruff 0.17.0, make lint e verificação de estilo no workflow.
Os ajustes de código se limitaram a formatação; os testes passaram a usar
zip(strict=True) para explicitar o pareamento de quatro categorias.

Uma tentativa inicial de consultar versões usou um subcomando indisponível
no uv instalado. Ruff foi instalado e sua versão efetiva foi fixada.
A primeira revisão do Ruff usou regras herdadas do ambiente e sugeriu alterar
o tipo de exceção de uma validação. Foi definida uma configuração explícita
para o projeto, preservando ValueError conforme o contrato já testado.
Os apontamentos de formatação e pareamento de sequências foram corrigidos.

make lint passou. Uma execução isolada teve 60 testes aprovados e um erro
de permissão na pasta temporária do Windows. A execução no contexto do usuário
teve 61 aprovados. A suíte também teve 61 aprovados em Python 3.11.17.

O README ganhou trechos literais do pedido original, efeitos das decisões,
relato de dificuldades reais e justificativas de arquitetura/SRP/DRY.
Não foram inventadas métricas de produtividade nem novos prompts.

A tentativa de captura no navegador foi encerrada pela ferramenta por não
conseguir determinar a URL atual com segurança. A automação de interface foi
interrompida. Foram produzidos relatórios visuais a partir de stdout/stderr
reais, identificados explicitamente como renderizações, não como screenshots
nativos. A senha foi omitida antes de salvar qualquer evidência.
Capturas nativas da CLI e dos testes permanecem pendentes.

Para manter dez commits, esta finalização é reunida no último commit da entrega.
A atualização mantém o histórico de desenvolvimento anterior, sem inventar TDD.
A tag v1.0.0 e os pacotes devem acompanhar o estado validado após a publicação.
