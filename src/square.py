from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side: int | float) -> None:
        if side <= 0:
            raise ValueError("side must be positive")

        super().__init__(side, side)
