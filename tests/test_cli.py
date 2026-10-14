import os
import string
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def executar(*argumentos):
    return subprocess.run(
        [sys.executable, str(ROOT / "main.py"), *argumentos],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "PYTHONUTF8": "1"},
        cwd=ROOT,
        timeout=10,
        check=False,
    )


@pytest.mark.parametrize(
    "argumentos,tamanho,grupos",
    [
        (
            [],
            16,
            [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation],
        ),
        (
            ["--tamanho", "20"],
            20,
            [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation],
        ),
        (
            ["--tamanho", "12", "--maiusculas", "--numeros"],
            12,
            [string.ascii_uppercase, string.digits],
        ),
        (
            ["--tamanho", "16", "--minusculas", "--maiusculas", "--numeros", "--simbolos"],
            16,
            [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation],
        ),
        (["--tamanho", "1", "--numeros"], 1, [string.digits]),
        (["--tamanho", "128", "--simbolos"], 128, [string.punctuation]),
    ],
)
def test_comandos_validos(argumentos, tamanho, grupos):
    resultado = executar(*argumentos)
    assert resultado.returncode == 0
    assert resultado.stderr == ""
    assert resultado.stdout.endswith("\n")
    senha = resultado.stdout.rstrip("\n")
    assert len(senha) == tamanho
    assert set(senha) <= set("".join(grupos))
    assert all(any(c in grupo for c in senha) for grupo in grupos)


@pytest.mark.parametrize(
    "argumentos,mensagem",
    [
        (["--tamanho", "0"], "entre 1 e 128"),
        (["--tamanho", "-1"], "entre 1 e 128"),
        (["--tamanho", "129"], "entre 1 e 128"),
        (["--tamanho", "abc"], "número inteiro"),
        (["--tamanho", "1.5"], "número inteiro"),
        (["--tamanho", "3"], "categorias selecionadas"),
        (["--tamanho", "1", "--minusculas", "--numeros"], "categorias selecionadas"),
        (["--tamanho"], "é necessário informar um valor"),
        (["--desconhecido"], "argumentos não reconhecidos"),
        (["--min"], "argumentos não reconhecidos"),
        (["--numeros=sim"], "valor explícito não permitido"),
    ],
)
def test_erros_em_portugues_sem_senha(argumentos, mensagem):
    resultado = executar(*argumentos)
    assert resultado.returncode == 2
    assert resultado.stdout == ""
    assert "erro:" in resultado.stderr
    assert mensagem in resultado.stderr
    assert "uso:" in resultado.stderr


@pytest.mark.parametrize("opcao", ["--help", "-h"])
def test_ajuda_em_portugues(opcao):
    resultado = executar(opcao)
    assert resultado.returncode == 0
    assert resultado.stderr == ""
    assert "uso:" in resultado.stdout
    assert "opções:" in resultado.stdout
    assert "Exemplos:" in resultado.stdout
    for flag in ["--tamanho", "--minusculas", "--maiusculas", "--numeros", "--simbolos"]:
        assert flag in resultado.stdout


def test_cli_funciona_fora_da_pasta_do_projeto(tmp_path):
    resultado = subprocess.run(
        [sys.executable, str(ROOT / "main.py"), "--tamanho", "8", "--numeros"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "PYTHONUTF8": "1"},
        cwd=tmp_path,
        timeout=10,
        check=False,
    )
    assert resultado.returncode == 0
    assert len(resultado.stdout.rstrip("\n")) == 8
    assert set(resultado.stdout.rstrip("\n")) <= set(string.digits)
    # A execução bem-sucedida não cria arquivos na pasta de trabalho do usuário.
    assert list(tmp_path.iterdir()) == []
