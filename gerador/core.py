"""Geração de senhas com escolhas e embaralhamento criptograficamente seguros."""

import secrets
import string


def gerar_senha(
    tamanho: int = 16,
    *,
    minusculas: bool = False,
    maiusculas: bool = False,
    numeros: bool = False,
    simbolos: bool = False,
) -> str:
    """Gerar uma senha; sem categorias explícitas, usar as quatro.

    O tamanho deve ser inteiro de 1 a 128 e comportar todas as categorias.
    Levanta ValueError para entradas inválidas. Não imprime nem persiste senhas.
    """
    if not isinstance(tamanho, int) or isinstance(tamanho, bool):
        raise ValueError("O tamanho deve ser um número inteiro.")
    if not 1 <= tamanho <= 128:
        raise ValueError("O tamanho deve estar entre 1 e 128 caracteres.")

    categorias = [
        grupo
        for grupo, selecionado in (
            (string.ascii_lowercase, minusculas),
            (string.ascii_uppercase, maiusculas),
            (string.digits, numeros),
            (string.punctuation, simbolos),
        )
        if selecionado
    ]
    if not categorias:
        categorias = [
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.digits,
            string.punctuation,
        ]
    if tamanho < len(categorias):
        raise ValueError(
            f"O tamanho deve ser pelo menos {len(categorias)} "
            "para incluir todas as categorias selecionadas."
        )

    caracteres = [secrets.choice(grupo) for grupo in categorias]
    alfabeto = "".join(categorias)
    caracteres.extend(secrets.choice(alfabeto) for _ in range(tamanho - len(categorias)))
    _embaralhar(caracteres)
    return "".join(caracteres)


def _embaralhar(caracteres: list[str]) -> None:
    """Aplicar Fisher–Yates in-place usando uma fonte criptográfica."""
    for indice in range(len(caracteres) - 1, 0, -1):
        destino = secrets.randbelow(indice + 1)
        caracteres[indice], caracteres[destino] = caracteres[destino], caracteres[indice]
