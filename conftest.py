import pytest


@pytest.fixture(
    params=[
        pytest.param(([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]), id="already_sorted"),
        pytest.param(([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]), id="reverse_sorted"),
        pytest.param(([0, 2, 1, 4, 3], [0, 1, 2, 3, 4]), id="mixed_order"),
        pytest.param(([], []), id="empty_list"),
    ]
)
def input_expected(request):
    return request.param
