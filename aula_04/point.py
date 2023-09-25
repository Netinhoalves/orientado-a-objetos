# class Point:
#     pass
# p1 = Point()
# p2 = Point()
# p1.x = 5
# p1.y = 4
# p2.x = 3
# p2.y = 6
# print(p1.x, p1.y)
# print(p2.x, p2.y)

# class Point:
#     def reset (self):
#         self.x = 0
#         self.y = 0
# p = Point()
# p.reset()
# print(p.x, p.y)

class Point:
    "Representa um ponto em coordenadas geométricas bidimensionais."
 
    def __init__(self, x=0, y=0):
        """Inicializa a posição de um novo ponto. As coordenadas x e y
           podem ser especificadas. Se não forem, o
           ponto assume a origem."""
        self.move(x, y)
 
    def move(self, x, y):
        "Move o ponto para uma nova localização no espaço 2D."
        self.x = x
        self.y = y
 
    def reset(self):
        "Redefine o ponto para a origem geométrica: 0, 0."
        self.move(0, 0)
 
    def calculate_distance(self, other_point):
        """Calcula a distância deste ponto para um segundo
        ponto passado como parâmetro.
 
        Esta função usa o Teorema de Pitágoras para calcular
        a distância entre os dois pontos. A distância é
        retornada como um número float."""
 
        return (
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        ) ** (1/2)
 
 
# como usar:
point1 = Point()
point2 = Point()
 
point1.reset()
point2.move(5, 0)
print(point2.calculate_distance(point1))
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))