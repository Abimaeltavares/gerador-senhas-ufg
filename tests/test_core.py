import string
from itertools import product

import pytest

from gerador.core import gerar_senha

OPCOES = ("minusculas", "maiusculas", "numeros", "simbolos")
CATEGORIAS = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)


@pytest.mark.parametrize("selecao", list(product((False, True), repeat=4)))
def test_categorias_e_alfabeto_permitido(selecao):
    categorias = [grupo for grupo, ativa in zip(CATEGORIAS, selecao) if ativa]
    categorias = categorias or list(CATEGORIAS)
    senha = gerar_senha(20, **dict(zip(OPCOES, selecao)))
    assert len(senha) == 20
    assert set(senha) <= set("".join(categorias))
    assert all(any(caractere in grupo for caractere in senha) for grupo in categorias)


def test_tamanho_padrao():
    assert len(gerar_senha()) == 16


@pytest.mark.parametrize("tamanho", [4, 16, 64, 128])
def test_tamanho_exato_e_limites_com_todas_as_categorias(tamanho):
    assert len(gerar_senha(tamanho)) == tamanho


@pytest.mark.parametrize("opcao", OPCOES)
def test_categoria_unica_permite_tamanho_um(opcao):
    assert len(gerar_senha(1, **{opcao: True})) == 1


@pytest.mark.parametrize("tamanho", [0, -1, -100, 129, 1000])
def test_rejeita_tamanho_fora_dos_limites(tamanho):
    with pytest.raises(ValueError, match="entre 1 e 128"):
        gerar_senha(tamanho)


@pytest.mark.parametrize("tamanho", [True, False, 1.5, "16", None])
def test_rejeita_tamanho_que_nao_e_inteiro(tamanho):
    with pytest.raises(ValueError, match="inteiro"):
        gerar_senha(tamanho)


@pytest.mark.parametrize(
    "tamanho,opcoes",
    [(3, {}), (1, {"minusculas": True, "numeros": True}),
     (2, {"minusculas": True, "maiusculas": True, "simbolos": True})],
)
def test_rejeita_tamanho_insuficiente_para_categorias(tamanho, opcoes):
    with pytest.raises(ValueError, match="categorias selecionadas"):
        gerar_senha(tamanho, **opcoes)


def test_execucoes_apresentam_variacao_observada():
    senhas = {gerar_senha() for _ in range(20)}
    # Uma amostra observada; não é uma prova matemática de segurança.
    assert len(senhas) > 1


def test_usa_secrets_para_escolhas_e_embaralhamento(monkeypatch):
    import gerador.core as core

    escolhas = []
    limites = []

    def escolha_segura(alfabeto):
        escolhas.append(alfabeto)
        return alfabeto[0]

    def indice_seguro(limite):
        limites.append(limite)
        return 0

    monkeypatch.setattr(core.secrets, "choice", escolha_segura)
    monkeypatch.setattr(core.secrets, "randbelow", indice_seguro)
    senha = gerar_senha(4)
    assert escolhas == list(CATEGORIAS)
    assert limites == [4, 3, 2]
    assert senha == "A0!a"


def test_completa_senha_apenas_com_alfabeto_selecionado(monkeypatch):
    import gerador.core as core

    escolhas = []

    def escolha_segura(alfabeto):
        escolhas.append(alfabeto)
        return alfabeto[0]

    monkeypatch.setattr(core.secrets, "choice", escolha_segura)
    monkeypatch.setattr(core.secrets, "randbelow", lambda limite: limite - 1)
    senha = gerar_senha(4, numeros=True)
    assert escolhas == [string.digits] * 4
    assert senha == "0000"
