# Validação final — v1.0.0

Data: 13 de outubro de 2026, America/Sao_Paulo.
Ambiente: Windows, PowerShell 7.6.6.

## Resultados executados

| Verificação | Resultado |
|---|---|
| Núcleo antes da implementação | 41 falhas esperadas (Red) |
| Núcleo após implementação | 41 testes aprovados (Green) |
| Núcleo após extração do embaralhamento | 41 testes aprovados (Refactor) |
| Suíte completa, Python 3.12.15 | 61 testes aprovados |
| Suíte completa, Python 3.11.17 | 61 testes aprovados |
| make install, GNU Make 4.4.1 | Aprovado |
| make test | 61 testes aprovados |
| make run | Geração padrão aprovada, saída omitida |
| iniciar.cmd --tamanho 12 --maiusculas --numeros | Aprovado, saída omitida |
| python -m pip check | Nenhuma incompatibilidade identificada |

A primeira execução do verificador de make install usou a própria .venv e
falhou ao recriá-la no Windows. O verificador foi reexecutado com o Python-base
e passou. Não houve falha do algoritmo de geração.

Os testes da CLI executam todos os exemplos de utilização pedidos, além de
erros, ajuda e execução fora da pasta do projeto. Saídas de senha não são
salvas em relatórios.

## Revisão técnica

- [x] Fonte criptográfica: secrets.choice para caracteres e secrets.randbelow
  para índices do Fisher–Yates; sem random comum.
- [x] Categorias escolhidas garantidas, sem caracteres fora do alfabeto permitido.
- [x] Tamanho inteiro, positivo, no máximo 128 e suficiente para as categorias.
- [x] Nenhuma operação de arquivo, rede, banco ou log no núcleo ou na CLI.
- [x] Separação entre geração e interface.
- [x] Documentação da distribuição não uniforme e dos limites do MVP.
- [x] LICENSE, README, AGENTS.md, dependências fixadas e Makefile presentes.
- [x] Diário com resultados reais e etapas Red → Green → Refactor.
- [x] Rascunho de fórum sem link de publicação fictício.
- [x] Histórico real de sete commits significativos em Conventional Commits.
- [x] Tag local v1.0.0 preparada após as verificações.
- [x] Ambiente virtual, ferramentas, caches e arquivos sensíveis excluídos do Git.

## Pendências externas

- [ ] Aprovação do autor para publicação.
- [ ] Criar repositório público gerador-senhas-ufg e enviar commits/tag.
- [ ] Criar Release v1.0.0 e confirmar README renderizado e acesso sem login.
- [ ] Executar e conferir GitHub Actions. O workflow está preparado,
  mas não foi executado no serviço.
- [ ] Preencher o link real no rascunho do fórum após publicação.
- [ ] Revisão humana e compreensão do código pelo autor.
- [ ] Autor submeter no fórum e comentar o trabalho de um colega.

Não houve teste local em Linux nem em outras versões de Python.
Não foram produzidas métricas de produtividade, análise de entropia ou
afirmações de auditoria humana concluída.
