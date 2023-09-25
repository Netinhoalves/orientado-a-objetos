import math
import abc


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, outro):
        return math.sqrt((outro.x - self.x) ** 2 + (outro.y - self.y) ** 2)


class Linha:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def medida(self):
        return self.p1.distancia(self.p2)

    def coeficiente_angular(self):
        denominador = self.p2.x - self.p1.x
        if denominador == 0:
            return None
        numerador = self.p2.y - self.p1.y
        return numerador / denominador

    def eh_paralela(self, outra):
        return self.coeficiente_angular() == outra.coeficiente_angular()


class Poligono(abc.ABC):
    def __init__(self, lados):
        self.lados = lados

    def perimetro(self):
        soma = 0
        for lado in self.lados:
            soma += lado.medida()
        return soma

    @abc.abstractmethod
    def area(self):
        pass


class Triangulo(Poligono):
    def __init__(self, p1, p2, p3):
        lado1 = Linha(p1, p2)
        lado2 = Linha(p2, p3)
        lado3 = Linha(p3, p1)
        super().__init__([lado1, lado2, lado3])

    def semiperimetro(self):
        return self.perimetro() / 2

    def area(self):
        p = self.semiperimetro()
        a = self.lados[0]
        b = self.lados[1]
        c = self.lados[2]
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
