from pai.filho.b import B

from .filho.b import imprimir as b_imprimir


A = 10


def imprimir():
    print(__name__)


if __name__ == "__main__":
    print(A, B)
    imprimir()
    b_imprimir()
