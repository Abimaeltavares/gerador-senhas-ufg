"""Núcleo do gerador de senhas."""


def gerar_senha(
    tamanho: int = 16,
    *,
    minusculas: bool = False,
    maiusculas: bool = False,
    numeros: bool = False,
    simbolos: bool = False,
) -> str:
    """Gerar uma senha com pelo menos um caractere de cada categoria selecionada."""
    raise NotImplementedError("Núcleo ainda não implementado.")
