import pytest

from src.circle import Circle
from src.rectangle import Rectangle


@pytest.mark.figure
@pytest.mark.parametrize(
    ("figure_1", "sides_figure_1", "figure_2", "sides_figure_2", "expected_result"),
    [
        pytest.param(Rectangle, (3,4), Circle, (4, ), 62.27, id="rectangle area plus circle area")
    ]
)
def test_figure_add_area(figure_1, sides_figure_1, figure_2, sides_figure_2, expected_result):
    fig_1 = figure_1(*sides_figure_1)
    fig_2 = figure_2(*sides_figure_2)
    assert round(fig_1.add_area(fig_2), 2) == expected_result