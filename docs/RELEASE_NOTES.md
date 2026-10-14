# Gerador de Senhas Seguras v1.0.0

- CLI em português com tamanho padrão de 16 e limite máximo de 128.
- Seleção de quatro categorias e garantia de presença das escolhidas.
- Aleatoriedade com secrets.choice e embaralhamento com secrets.randbelow.
- Validação de entradas, ajuda e exemplos executáveis.
- 61 testes automatizados, documentação e diário com evidências reais de TDD.

A geração funciona sem dependências externas, rede ou armazenamento de senhas.
pytest é necessário somente para executar os testes.

Publicado com aprovação do autor.
Os quatro jobs do GitHub Actions foram aprovados em Windows/Ubuntu,
Python 3.11/3.12.

Repositório: https://github.com/Abimaeltavares/gerador-senhas-ufg
Evidência: https://github.com/Abimaeltavares/gerador-senhas-ufg/actions/runs/38488310328
