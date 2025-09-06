from .base import Figure
import math

class Circle(Figure):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("The radius must be positive.")
        self.radius = radius
        
    @property
    def area(self) -> float:
        return math.pi * self.radius ** 2

class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("The sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Such a triangle does not exist.")
        self.a, self.b, self.c = a, b, c

    @property
    def is_rectangular(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        print(list(map(lambda x: x**2, sides)))
        if math.isclose(sides[2] ** 2, (sides[1] ** 2) + (sides[0] ** 2)):
            return True
        return False
        
    @property
    def area(self) -> float:
        if self.is_rectangular:
            sides = sorted([self.a, self.b, self.c])
            return sides[0] * sides[1] / 2
        else:
            semiperimeter = (self.a + self.b + self.c) / 2
            return math.sqrt(
                semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c)
            )