import pytest


@pytest.fixture(
    params=[
        pytest.param(([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]), id="already_sorted"),
        pytest.param(([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]), id="reverse_sorted"),
        pytest.param(([0, 2, 1, 4, 3], [0, 1, 2, 3, 4]), id="mixed_order"),
        pytest.param(([], []), id="empty_list"),
        pytest.param(([1, 1, 1], [1, 1, 1]), id="all_duplicates"),
        pytest.param(([3, 1, 2, 1, 3], [1, 1, 2, 3, 3]), id="duplicates_mixed"),
        pytest.param(([10**6, -(10**6), 0], [-(10**6), 0, 10**6]), id="extreme_values"),
        pytest.param(([42], [42]), id="single_element"),
        pytest.param(([1, 2, 3, 5, 4], [1, 2, 3, 4, 5]), id="almost_sorted"),
        pytest.param(([2, 2, 2, 1, 2], [1, 2, 2, 2, 2]), id="one_outlier"),
        pytest.param(
            (list(range(100, 0, -1)), list(range(1, 101))), id="large_reverse"
        ),
        pytest.param(
            ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]), id="sorted_with_duplicates"
        ),
        pytest.param(([0, 0, 0, 1, -1], [-1, 0, 0, 0, 1]), id="zeros_mixed"),
    ]
)
def input_expected(request):
    return request.param
