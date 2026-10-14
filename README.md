# Gerador de Senhas Seguras

Mini projeto individual de CLI em Python para gerar senhas com tamanho e
categorias de caracteres escolhidos pelo usuário, com apoio de IA generativa
durante o desenvolvimento.

**Autor:** Abimaeltavares  
**Versão:** 1.0.0 · **Licença:** MIT · **Python:** 3.11 ou superior

Projeto desenvolvido para a Especialização em Engenharia de Software:
Automação e Inovação com Inteligência Artificial Generativa da UFG,
trilha Introdução Prática, com orientação do professor Ms. Leon Sólon da Silva.
Informações acadêmicas fornecidas pelo autor.

## Problema e objetivo

A criação manual de senhas pode produzir padrões previsíveis. O objetivo deste
MVP é gerar caracteres usando uma fonte criptograficamente segura, respeitando
as categorias solicitadas e verificando as entradas.

A aplicação funciona localmente, sem API, banco de dados ou conexão com a internet
durante a geração. Não salva senhas em arquivos, logs ou histórico próprio.

## Funcionalidades

- Tamanho padrão de 16 caracteres, com limite de 128.
- Seleção de minúsculas, maiúsculas, números e símbolos.
- Todas as categorias são usadas quando nenhuma é especificada.
- Pelo menos um caractere de cada categoria selecionada.
- Escolha de caracteres com `secrets.choice`.
- Embaralhamento Fisher–Yates com `secrets.randbelow`.
- Erros claros em português para entradas inválidas.
- Ajuda com `--help` e saída de sucesso contendo somente a senha.

## Tecnologias

| Tecnologia | Papel |
|---|---|
| Python 3.11+ | Linguagem e ambiente de execução |
| argparse | Argumentos e ajuda da CLI |
| secrets | Aleatoriedade criptográfica |
| string | Categorias de caracteres ASCII |
| pytest | Testes automatizados, somente no desenvolvimento |
| Ruff 0.17.0 | Estilo, importações e formatação, somente no desenvolvimento |
| Git | Histórico com Conventional Commits |

As dependências de desenvolvimento estão fixadas em `requirements.txt`, incluindo as
transitivas. Não há dependências externas de runtime.

## Arquitetura

```mermaid
flowchart LR
    Usuario[Usuário no terminal] --> CLI[main.py: argumentos e mensagens]
    CLI --> Core[gerador/core.py: validação e geração]
    Core --> Fonte[secrets: fonte do sistema operacional]
    Core --> CLI
    CLI --> Terminal[Senha ou erro em português]
```

```text
main.py                        Interface CLI
gerador/core.py                Geração, validação e embaralhamento
tests/test_core.py             Testes do núcleo
tests/test_cli.py              Testes reais da CLI por subprocesso
docs/arquitetura.md             Decisões de arquitetura
docs/diario-desenvolvimento.md  Registro das etapas e do TDD
AGENTS.md                      Instruções de escopo e qualidade
Makefile                       Comandos install, test, run e lint
docs/evidencias/                Relatórios visuais de execuções reais
iniciar.cmd                    Facilitador local no Windows
```


### Por que essa arquitetura?

Python atende ao ambiente Windows/PowerShell e oferece as bibliotecas do MVP
na instalação padrão. `argparse` implementa os argumentos e a ajuda; `secrets`
fornece a aleatoriedade adequada para a geração; `string` fornece os alfabetos
ASCII documentados. Não há dependências externas para gerar a senha.

A separação CLI/núcleo aplica **responsabilidade única (SRP)**: `main.py`
cuida da interação; `gerar_senha` valida e monta os caracteres; `_embaralhar`
aplica Fisher–Yates. A CLI reutiliza o núcleo, sem duplicar suas regras (DRY).
Não se afirma aplicar todos os princípios SOLID em um MVP funcional pequeno.

As decisões e seus motivos estão em [arquitetura.md](docs/arquitetura.md).

### Requisitos funcionais atendidos

| Requisitos | Comportamento |
|---|---|
| RF01 | Tamanho configurável, padrão de 16 caracteres |
| RF02–RF05 | Seleção das quatro categorias |
| RF06–RF07 | Todas por padrão e presença de cada categoria selecionada |
| RF08–RF09 | Escolha e embaralhamento com secrets |
| RF10–RF11 | Validação de tamanho e erros em português |
| RF12–RF13 | Saída no terminal, ajuda e exemplos |

## Requisitos

- Python 3.11 ou superior; recomendamos usar uma das versões verificadas
  indicadas na seção de testes.
- Git para clonar o repositório.
- Internet apenas para baixar Python e instalar as dependências de teste.
- GNU Make é opcional; comandos equivalentes são fornecidos abaixo.

## Instalação no Windows / PowerShell

Repositório público: [https://github.com/Abimaeltavares/gerador-senhas-ufg](https://github.com/Abimaeltavares/gerador-senhas-ufg).
[Release v1.0.0](https://github.com/Abimaeltavares/gerador-senhas-ufg/releases/tag/v1.0.0).
O acesso às páginas foi confirmado sem autenticação.

Com Python instalado e disponível pelo launcher `py`:

```powershell
git clone https://github.com/Abimaeltavares/gerador-senhas-ufg.git
cd gerador-senhas-ufg
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe main.py
```

Se estiver usando Python 3.11, substitua `py -3.12` por `py -3.11`.
Se o launcher não estiver disponível, use `python -m venv .venv`
com uma versão compatível instalada.

A ativação do ambiente virtual é opcional:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py --help
```

Se o PowerShell bloquear `Activate.ps1`, use diretamente
`.\.venv\Scripts\python.exe`, conforme os exemplos anteriores.
Não é necessário alterar a política de execução.

## Argumentos e exemplos

| Argumento | Comportamento |
|---|---|
| `--tamanho N` | Inteiro de 1 a 128; padrão 16 |
| `--minusculas` | Letras a-z |
| `--maiusculas` | Letras A-Z |
| `--numeros` | Dígitos 0-9 |
| `--simbolos` | Símbolos de `string.punctuation` |
| `--help`, `-h` | Ajuda e exemplos |

Em um terminal com o ambiente ativado:

```powershell
python main.py
python main.py --tamanho 20
python main.py --tamanho 12 --maiusculas --numeros
python main.py --tamanho 16 --minusculas --maiusculas --numeros --simbolos
python main.py --help
```

Todos esses exemplos são executados nos testes da CLI. As saídas aleatórias
não são reproduzidas na documentação.

Categorias explícitas restringem o alfabeto: `--maiusculas --numeros`
usa somente letras A-Z e números, com pelo menos um de cada.
Sem categorias, o mínimo é 4 caracteres. Com uma categoria, o mínimo é 1.

Exemplo inválido:

```powershell
.\.venv\Scripts\python.exe main.py --tamanho 3
```

Resultado: erro em português, sem senha, com código de saída 2.
Geração bem-sucedida e ajuda retornam código 0. No PowerShell, consulte
`$LASTEXITCODE` imediatamente após a execução.

## Testes

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Com GNU Make e Python disponíveis:

```powershell
make install PYTHON=python
make lint
make test
make run
```

A suíte possui **61 testes**: 41 do núcleo e 20 da CLI. Verifica tamanho,
as 16 combinações de seleção, caracteres permitidos, presença das categorias,
limites, erros, variação observada e chamadas às fontes criptográficas.
Os testes da CLI executam processos reais e verificam retorno, stdout e stderr.

O comando `make lint` executa `ruff check .` e `ruff format --check .`.
Sem GNU Make, use:

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
```

O teste de variação é uma observação de amostra, com probabilidade desprezível
de colisão total. Não prova segurança matemática nem exige que duas gerações
sempre sejam diferentes. Os testes com fontes controladas verificam chamadas
a `secrets.choice` e `secrets.randbelow`; não avaliam a entropia do sistema operacional.

O ciclo Red → Green → Refactor do núcleo foi executado e registrado no
[diário](docs/diario-desenvolvimento.md). Os resultados finais e versões
verificadas constam em [VALIDACAO.md](docs/VALIDACAO.md).

O GitHub Actions executou os 61 testes em Windows e Ubuntu, com Python
3.11 e 3.12. As quatro combinações foram aprovadas.
[Execução verificada](https://github.com/Abimaeltavares/gerador-senhas-ufg/actions/runs/38488310328).


## Evidências visuais de execução

As imagens abaixo são **relatórios renderizados de saídas reais**, executadas
em Windows em 14/10/2026. Não são capturas nativas do terminal.
Os comandos, stdout/stderr e códigos de saída estão registrados em texto
junto das imagens. A senha da demonstração foi omitida em memória antes de
salvar qualquer relatório.

Para cumprir literalmente a exigência de screenshots do curso, ainda é
necessário complementar estes relatórios com capturas nativas da CLI e dos testes.

### Ajuda da CLI

![Relatório real da ajuda](docs/evidencias/ajuda.png)

[Saída textual](docs/evidencias/ajuda.txt).

### Geração de demonstração

![Relatório real de geração com senha omitida](docs/evidencias/geracao.png)

[Verificações registradas](docs/evidencias/geracao.txt).

### Entrada inválida

![Relatório real de validação de tamanho](docs/evidencias/entrada-invalida.png)

[Saída textual](docs/evidencias/entrada-invalida.txt).

### Análise estática e testes

![Relatório real de make lint e make test](docs/evidencias/testes.png)

[Saída textual](docs/evidencias/testes.txt).

## IA generativa no ciclo de vida

A IA, pelo Codex, apoiou a interpretação dos requisitos, arquitetura,
testes, implementação, refatoração, revisão e documentação.

| Etapa | Apoio da IA | Evidência |
|---|---|---|
| Planejamento | Escopo e separação CLI/núcleo | Arquitetura e AGENTS.md |
| Testes | Casos válidos, inválidos e fontes seguras | tests/ e fase Red real |
| Implementação | Validações, geração e CLI | Código e fase Green |
| Refatoração | Extração do embaralhamento | Commit e reexecução dos testes |
| Revisão | Leitura do código e conferência de comandos | Diário e validação |
| Documentação | README e diário | docs/ |

A participação humana observada foi definir requisitos, escolher o tema,
solicitar planejamento e autorizar a execução. O autor ainda deve compreender
e revisar o código antes de apresentar; não se declara revisão humana concluída.

O pedido foi analisado por elementos do CO-STAR: contexto acadêmico, objetivo
de gerar senhas, estilo simples, tom em português, público do projeto e resposta
esperada com código, testes e documentação. Essa é uma análise do pedido real,
não um novo prompt inventado como se tivesse sido enviado pelo autor.


### Trechos reais dos pedidos e seus efeitos

Os trechos abaixo vêm do texto de requisitos enviado pelo autor nesta conversa.
São trechos de um único pedido real, não uma sequência de prompts inventada.

> “Não utilizar random comum para gerar senhas.”

Essa restrição guiou a escolha de `secrets.choice` e `secrets.randbelow`.
A revisão conferiu o código e os testes controlam essas chamadas para verificar
que a escolha de caracteres e o embaralhamento usam as funções previstas.

> “Organizar o código separando a lógica de geração da interface CLI.”

A implementação foi dividida em `main.py` e `gerador/core.py`.
A refatoração extraiu o embaralhamento para uma função separada. Os testes do
núcleo continuaram aprovados após essa mudança.

> “Não afirmar que testes passaram sem executá-los.”

O diário registra a execução com 41 falhas antes da implementação e as
execuções Green e Refactor aprovadas. A suíte completa possui 61 testes
realmente executados; a documentação diferencia resultados locais e do GitHub.

### Dificuldades verificadas e revisão das sugestões

Na verificação de `make install`, um script estava sendo executado pela própria
`.venv` que o comando tentava recriar. O Windows manteve o executável ocupado.
O verificador foi executado com o Python-base, fora da `.venv`, e os comandos
passaram. Essa foi uma dificuldade de verificação do ambiente, não um defeito
de geração de senhas.

Ao adicionar Ruff, foram ajustados formatação e os dois `zip` dos testes,
com `strict=True` para explicitar que as sequências têm o mesmo tamanho.
As validações existentes foram preservadas e os 61 testes passaram novamente.
Uma execução isolada teve erro de permissão na pasta temporária; a repetição
no contexto do usuário passou, sem afrouxar o teste.

A IA ajudou a diagnosticar e propor ajustes. Suas saídas foram verificadas
por testes e leitura do código, não aceitas como prova por si só.
Não houve medição de tempo economizado nem percentual de produtividade;
esses números não foram inventados.

## Segurança e limitações

- A aleatoriedade vem de `secrets`, apropriado para senhas segundo a
  [documentação oficial do Python](https://docs.python.org/3/library/secrets.html).
- Não se usa `random` comum para caracteres ou embaralhamento.
- A aplicação não persiste senhas. Elas aparecem no terminal; redirecionamentos
  feitos pelo usuário e o histórico visual do terminal ficam fora desse controle.
- A força de uma senha depende do tamanho e do alfabeto escolhido. Aceitar
  uma senha curta para testar limites não garante que ela seja adequada ao uso real.
- A construção garante categorias e mistura as posições, mas não promete
  uniformidade entre todas as senhas possíveis que satisfazem a restrição.
- Símbolos incluem aspas, barras e outros caracteres ASCII; sites podem ter
  regras diferentes. Não há exclusão personalizada de símbolos neste MVP.
- Não há avaliação de senhas existentes, armazenamento, clipboard nem interface web.
- Próximos passos possíveis: exclusão de caracteres ambíguos e escolha de símbolos
  permitidos, somente após uma nova definição de escopo.

## Créditos e licença

Autor: Abimaeltavares. Implementação assistida por Codex.
Licença [MIT](LICENSE).

Referências:
[secrets](https://docs.python.org/3/library/secrets.html),
[argparse](https://docs.python.org/3/library/argparse.html),
[pytest](https://docs.pytest.org/en/stable/),
[Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/).
