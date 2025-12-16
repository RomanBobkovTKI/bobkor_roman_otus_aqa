import pytest

from src.triangle import Triangle


@pytest.mark.triangle
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "expected"),
    [
        pytest.param(1, 2, 2, 0.97, id="int size"),
        pytest.param(2.5, 2.5, 1.1, 1.34, id="float size"),
    ],
)
def test_triangle_area(side_a, side_b, side_c, expected):
    triangle = Triangle(side_a, side_b, side_c)
    assert round(triangle.area, 2) == expected


@pytest.mark.triangle
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "expected"),
    [
        pytest.param(1, 2, 2, 5, id="int size"),
        pytest.param(2.5, 2.5, 1.1, 6.1, id="float size"),
    ],
)
def test_triangle_perimeter(side_a, side_b, side_c, expected):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.perimeter == expected


@pytest.mark.triangle
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        pytest.param(-1, 2, 2, id="first negative value"),
        pytest.param(1, -2, 2, id="second negative value"),
        pytest.param(1, 2, -2, id="third negative value"),
        pytest.param(0, 0, 0, id="zero sizes"),
    ],
)
def test_triangle_negative_side(side_a, side_b, side_c):
    with pytest.raises(
        ValueError, match="side_a and side_b and side_c must be positive"
    ):
        Triangle(side_a, side_b, side_c)


@pytest.mark.triangle
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        pytest.param(4, 1, 1, id="impossible sides"),
        pytest.param(2, 2, 9, id="impossible sides"),
        pytest.param(10, 10, 100, id="impossible sides"),
    ],
)
def test_triangle_impossible_side(side_a, side_b, side_c):
    with pytest.raises(ValueError, match="sides dont be a triangle"):
        Triangle(side_a, side_b, side_c)
