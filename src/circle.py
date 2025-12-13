import math

from figure import Figure


class Circle(Figure):
    def __init__(self, radius: int | float):
        if radius <= 0:
            raise ValueError("radius must be positive")

        self.radius = radius

    @property
    def area(self):
        return (self.radius**2) * math.pi

    @property
    def perimeter(self):
        return 2 * self.radius * math.pi
