import pytest

from model.algos.buildin_sorted import buildin_sorted


@pytest.mark.parametrize(
    "test, result", [([2, 1, 4], [1, 2, 4]), ([4, 1, 2], [1, 2, 4])]
)
def test_buildin_sort(test, result):
    assert buildin_sorted(test) == result
