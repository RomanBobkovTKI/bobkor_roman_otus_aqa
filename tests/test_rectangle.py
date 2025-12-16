import pytest

from src.rectangle import Rectangle


@pytest.mark.rectangle
@pytest.mark.parametrize(
    ("side_a", "side_b", "expected"),
    [
        pytest.param(1, 1, 1, id="one int size side"),
        pytest.param(15, 20, 300, id="different int size side"),
        pytest.param(1.5, 1.5, 2.25, id="one float size side"),
        pytest.param(10.5, 11.25, 118.125, id="different float size side"),
        pytest.param(1.5, 5, 7.5, id="float size and int size"),
    ],
)
def test_rectangle_area(side_a, side_b, expected):
    r = Rectangle(side_a, side_b)
    assert r.area == expected, f"{r.side_a} * {r.side_b} = {r.area}"


@pytest.mark.rectangle
@pytest.mark.parametrize(
    ("side_a", "side_b", "expected"),
    [
        pytest.param(1, 1, 4, id="one int size side"),
        pytest.param(15, 20, 70, id="different int size side"),
        pytest.param(1.5, 1.5, 6, id="one float size side"),
        pytest.param(10.5, 11.25, 43.5, id="different float size side"),
        pytest.param(1.5, 5, 13, id="float size and int size"),
    ],
)
def test_rectangle_perimeter(side_a, side_b, expected):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == expected, f"({r.side_a} + {r.side_b}) * 2 = {r.perimeter}"


@pytest.mark.rectangle
@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        pytest.param(-1, 1, id="first side negative"),
        pytest.param(10, -10, id="second side negative"),
        pytest.param(-10, -10, id="negative sides"),
        pytest.param(0, -10, id="zero side with negative value"),
        pytest.param(-10, 0, id="zero side with negative value"),
        pytest.param(0, 0, id="zero sides"),
    ],
)
def test_rectangle_negative_sides(side_a, side_b):
    with pytest.raises(ValueError, match="side_a and side_b must be positive"):
        Rectangle(side_a, side_b)
