from recatngle import Rectangle


class Square(Rectangle):
    def __init__(self, side: int | float):
        if side <= 0:
            raise ValueError("side must be positive")

        super().__init__(side, side)
