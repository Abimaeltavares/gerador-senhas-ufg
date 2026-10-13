# Rascunho para o fórum avaliativo

Antes de enviar, publicar o projeto com aprovação do autor, preencher o link
e revisar o texto com suas próprias palavras. Não postar automaticamente.

## Texto sugerido

Meu mini projeto é o **Gerador de Senhas Seguras**, uma aplicação de linha
de comando em Python. Permite escolher o tamanho da senha e selecionar letras
minúsculas, maiúsculas, números e símbolos. Quando nenhuma categoria é indicada,
todas são usadas. A geração utiliza secrets e garante pelo menos um caractere
de cada categoria escolhida.

Repositório público: **[PREENCHER APÓS PUBLICAÇÃO]**.

Utilizei o Codex como apoio ao planejamento, à criação de testes, à implementação,
à refatoração e à documentação. Eu defini os requisitos e autorizei o desenvolvimento.
O núcleo foi trabalhado em um ciclo Red → Green → Refactor, com as falhas iniciais
e as execuções seguintes registradas no diário. Ao final, os 61 testes passaram
nas versões de Python informadas no relatório de validação.

Uma dificuldade concreta foi que Python não estava disponível no ambiente
inspecionado. Ele foi preparado em uma pasta local do projeto, com um ambiente
virtual separado. A execução foi documentada sem exigir ativação de scripts
PowerShell. Também foi necessário distinguir o acesso ao GitHub do ambiente
isolado do acesso disponível no Windows.

As sugestões da IA foram verificadas pela leitura do código e pelos testes.
Conferimos o uso de secrets tanto para escolher caracteres quanto para embaralhar,
a rejeição de tamanhos inválidos e a ausência de persistência de senhas.
O README apresenta instalação, comandos, decisões e limitações. A variação
observada em algumas execuções não foi tratada como prova de segurança.

## Antes da submissão

- Confirmar o link público, a renderização do README e a Release.
- Ler e compreender o código; ajustar o texto para refletir sua revisão.
- Enviar pelo fórum indicado no curso.
- Comentar o trabalho real de pelo menos um colega após lê-lo. Esse comentário
  não foi produzido aqui, pois nenhum trabalho de colega foi fornecido.

Prazo informado pelo autor: 19 de outubro de 2026, às 12h. Confirmar no ambiente
da disciplina; o prazo não foi verificado com uma fonte institucional.
