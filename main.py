"""Interface de linha de comando do Gerador de Senhas Seguras."""

import argparse
import sys
from collections.abc import Sequence

from gerador.core import gerar_senha


class ParserPortugues(argparse.ArgumentParser):
    """Adaptar ajuda e os erros comuns do argparse para português."""

    def format_usage(self) -> str:
        return super().format_usage().replace("usage:", "uso:", 1)

    def format_help(self) -> str:
        return super().format_help().replace("usage:", "uso:", 1)

    def error(self, message: str) -> None:
        traducoes = {
            "unrecognized arguments:": "argumentos não reconhecidos:",
            "expected one argument": "é necessário informar um valor",
            "ignored explicit argument": "valor explícito não permitido",
            "argument ": "argumento ",
        }
        for original, traducao in traducoes.items():
            message = message.replace(original, traducao)
        self.print_usage(sys.stderr)
        self.exit(2, f"erro: {message}\n")


def _inteiro(valor: str) -> int:
    try:
        return int(valor)
    except ValueError as error:
        raise argparse.ArgumentTypeError("o tamanho deve ser um número inteiro.") from error


def criar_parser() -> argparse.ArgumentParser:
    """Construir os argumentos públicos e seus exemplos de utilização."""
    parser = ParserPortugues(
        prog="main.py",
        description="Gere senhas aleatórias com uma fonte criptograficamente segura.",
        epilog=(
            "Exemplos:\n"
            "  python main.py\n"
            "  python main.py --tamanho 20\n"
            "  python main.py --tamanho 12 --maiusculas --numeros\n"
            "  python main.py --tamanho 16 --minusculas --maiusculas --numeros --simbolos\n"
            "Sem categorias explícitas, são utilizadas todas as quatro categorias."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=False,
        allow_abbrev=False,
    )
    parser._positionals.title = "argumentos posicionais"
    parser._optionals.title = "opções"
    parser.add_argument("-h", "--help", action="help", help="mostrar esta ajuda e sair")
    parser.add_argument(
        "--tamanho",
        type=_inteiro,
        default=16,
        metavar="N",
        help="tamanho de 1 a 128, suficiente para as categorias (padrão: 16)",
    )
    parser.add_argument("--minusculas", action="store_true", help="incluir letras minúsculas (a-z)")
    parser.add_argument("--maiusculas", action="store_true", help="incluir letras maiúsculas (A-Z)")
    parser.add_argument("--numeros", action="store_true", help="incluir números (0-9)")
    parser.add_argument("--simbolos", action="store_true", help="incluir símbolos ASCII")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Executar a CLI; exibir somente a senha em caso de sucesso."""
    parser = criar_parser()
    argumentos = parser.parse_args(argv)
    try:
        senha = gerar_senha(**vars(argumentos))
    except ValueError as error:
        parser.error(str(error))
    print(senha)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
