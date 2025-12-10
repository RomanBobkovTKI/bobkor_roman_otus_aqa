import math

from figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("side_a and side_b and side_c must be positive")

        if (
            side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_c + side_b <= side_a
        ):
            raise ValueError("sides dont be a triangle")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        half_perimetr = self.perimeter / 2
        return math.sqrt(
            half_perimetr
            * (half_perimetr - self.side_a)
            * (half_perimetr - self.side_b)
            * (half_perimetr - self.side_c)
        )

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
