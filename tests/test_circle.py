import pytest

from src.circle import Circle


@pytest.mark.circle
@pytest.mark.parametrize(
    ("radius", "expected"),
    [
        pytest.param(2, 12.57, id="int radius"),
        pytest.param(4.5, 63.62, id="float radius"),
    ],
)
def test_circle_area(radius, expected):
    circle = Circle(radius)
    assert round(circle.area, 2) == expected


@pytest.mark.parametrize(
    ("radius", "expected"),
    [
        pytest.param(5, 31.42, id="int radius"),
        pytest.param(4.5, 28.27, id="float radius"),
    ],
)
@pytest.mark.circle
def test_circle_perimeter(radius, expected):
    circle = Circle(radius)
    assert round(circle.perimeter, 2) == expected


@pytest.mark.circle
@pytest.mark.parametrize(
    "radius",
    [
        pytest.param(-1, id="negative value"),
        pytest.param(0, id="zro value"),
    ],
)
def test_circle_negative_radius(radius):
    with pytest.raises(ValueError, match="radius must be positive"):
        Circle(radius)


@pytest.mark.circle
@pytest.mark.parametrize(
    ("radius_1", "radius_2", "expected"),
    [
        pytest.param(5, 4.5, 142.16, id="int and float radiuses"),
    ],
)
def test_circle_add_area(radius_1, radius_2, expected):
    circle_1 = Circle(radius_1)
    circle_2 = Circle(radius_2)
    result = round(circle_1.add_area(circle_2), 2)
    assert result == expected
