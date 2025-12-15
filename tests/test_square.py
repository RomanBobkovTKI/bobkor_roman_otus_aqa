import pytest

from src.square import Square


@pytest.mark.square
@pytest.mark.parametrize(
    ("side", "expected"),
    [
        pytest.param(5, 25, id="int size"),
        pytest.param(5.5, 30.25, id="float size"),
    ]
)
def test_square_area(side, expected):
    square = Square(side)
    assert square.area == expected, f"{side} * 4 = {square.area}"

@pytest.mark.square
@pytest.mark.parametrize(
    ("side", "expected"),
    [
        pytest.param(5, 20, id="int size"),
        pytest.param(5.5, 22.0, id="float size"),
    ]
)
def test_square_perimeter(side, expected):
    square = Square(side)
    assert square.perimeter == expected, f"{side} * 4 = {square.perimeter}"

@pytest.mark.square
@pytest.mark.parametrize(
    "side",
    [
        pytest.param(-5, id="negative side"),
    ]
)
def test_square_negative_side(side):
    with pytest.raises(ValueError, match = "side must be positive"):
        Square(side),


@pytest.mark.square
@pytest.mark.parametrize(
    ("side_a", "side_b", "expected"),
    [
        pytest.param(5, 3, 34, id="int size"),
        pytest.param(5.5, 3.3, 41.14, id="float size"),
    ]
)
def test_square_add_figure(side_a, side_b, expected):
    square_1 = Square(side_a)
    square_2 = Square(side_b)
    result = square_1.add_area(square_2)
    assert result == expected, f"{side_a} * {side_a} + {side_b} * {side_b} = {expected}"