from enum import Enum


class Planet(Enum):
    MERCURY = (3.303e23, 2.4397e6)
    VENUS = (4.869e24, 6.0518e6)
    EARTH = (5.976e24, 6.37814e6)
    MARS = (6.421e23, 3.3972e6)
    JUPITER = (1.9e27, 7.1492e7)
    SATURN = (5.688e26, 6.0268e7)
    URANUS = (8.686e25, 2.5559e7)
    NEPTUNE = (1.024e26, 2.4746e7)

    def __init__(self, mass, radius):
        self.mass = mass  # in kilograms
        self.radius = radius  # in meters

    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300e-11
        return G * self.mass / (self.radius * self.radius)

    def surface_weight(self, otherMass):
        return otherMass * self.surface_gravity()




earth_weight = float(input("What is your weight on Earth? "))
mass = earth_weight / Planet.EARTH.surface_gravity()
for p in Planet:
    print(f"Your weight on {p.name} is {p.surface_weight(mass)}")


plutao = Planet(123893485913857832,13652665326)
