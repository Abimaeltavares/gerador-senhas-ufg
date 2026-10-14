# Instruções do projeto

- Escopo: gerador de senhas CLI em Python 3.11+, mensagens e documentação em português.
- Runtime apenas com argparse, secrets e string; não adicionar APIs, banco, web ou Docker.
- Separar interface CLI e núcleo. Manter funções pequenas e evitar abstrações desnecessárias.
- Usar secrets.choice e embaralhamento com secrets.randbelow. Não usar random comum.
- Validar tamanho inteiro de 1 a 128 e mínimo de uma posição por categoria selecionada.
- Sem categorias explícitas, usar minúsculas, maiúsculas, números e símbolos.
- Garantir pelo menos um caractere de cada categoria selecionada.
- Não salvar senhas em arquivos, logs ou histórico da aplicação. Exemplos usam saídas omitidas.
- Testar comportamento e uso das fontes seguras com pytest. Executar testes antes de declarar aprovação.
- Praticar Red → Green → Refactor quando viável e registrar apenas evidências reais no diário.
- Manter diário de decisões, comandos, resultados e participação humana, sem métricas inventadas.
- Commits reais e significativos em Conventional Commits. Não fabricar histórico ou resultados.
- Não apagar arquivos existentes nem executar ações destrutivas sem autorização.
- Preparar documentação e tag local v1.0.0 após validação.
- Pedir aprovação do autor antes de publicar no GitHub ou criar uma Release.
