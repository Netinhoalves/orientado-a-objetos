from pai.filho.b import B

from ..b import imprimir as b_imprimir


C = 30


def imprimir():
    print(__name__)


if __name__ == "__main__":
    print(C, B)
    imprimir()
    b_imprimir()
