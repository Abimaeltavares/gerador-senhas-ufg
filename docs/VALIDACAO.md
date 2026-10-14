# Validação final — v1.0.0

Atualização: 14 de outubro de 2026, America/Sao_Paulo.
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
| make lint, Ruff 0.17.0 | Análise estática e formatação aprovadas |
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
- [x] Histórico real com mais de cinco commits significativos em Conventional Commits.
- [x] Tag local v1.0.0 preparada após as verificações.
- [x] Ambiente virtual, ferramentas, caches e arquivos sensíveis excluídos do Git.

## Publicação e pendências externas

- [x] Aprovação do autor para publicação: resposta “sim” nesta sessão.
- [x] Repositório público criado, commits e tag enviados.
- [x] Release v1.0.0 publicada; páginas acessíveis sem autenticação.
  README renderizado confirmado pelo HTML servido pelo GitHub, com tabelas.
- [x] GitHub Actions: quatro jobs aprovados, Windows/Ubuntu e Python 3.11/3.12.
  [Evidência](https://github.com/Abimaeltavares/gerador-senhas-ufg/actions/runs/38488310328).
- [ ] Revisão humana e compreensão do código pelo autor.

Não houve teste local em Linux nem em outras versões de Python.
Não foram produzidas métricas de produtividade, análise de entropia ou
afirmações de auditoria humana concluída.

Repositório: https://github.com/Abimaeltavares/gerador-senhas-ufg
Release: https://github.com/Abimaeltavares/gerador-senhas-ufg/releases/tag/v1.0.0

A tag v1.0.0 e o ZIP da Release representam a documentação atual da entrega.
O código executável permanece o mesmo que foi validado pelos testes.

## Complementação dos critérios de documentação

- [x] Exemplos reais dos pedidos do autor no README, sem transcrição inventada.
- [x] Decisões de stack, responsabilidade única e DRY justificadas.
- [x] Ruff fixado em requirements.txt; make lint e verificação no CI configurados.
- [x] 61 testes aprovados novamente em Python 3.11.17 e 3.12.15.
- [x] Quatro imagens renderizadas de saídas reais, com a senha omitida antes de salvar.
- [ ] Capturas nativas de terminal para a exigência literal de screenshots do curso.

A captura de navegador foi interrompida pela ferramenta por não conseguir
determinar a URL atual com segurança. Não se contornou o bloqueio. Os relatórios
foram identificados como imagens renderizadas e não apresentados como screenshots.
A análise local passou. Os resultados do CI por versão estão disponíveis na aba Actions.
