from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    @property
    def area(self) -> int | float:
        pass

    @abstractmethod
    @property
    def perimeter(self) -> int | float:
        pass

    def add_area(self, other_figure) -> int | float:
        if not isinstance(other_figure, Figure):
            raise TypeError("other_figure must be of type Figure")

        return self.area + other_figure.area
