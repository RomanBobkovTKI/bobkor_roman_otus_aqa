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
