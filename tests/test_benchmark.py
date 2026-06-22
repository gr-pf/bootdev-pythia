import pytest
from statistics import StatisticsError

from model.benchmark import get_results


def test_get_results(params_get_results):
    input_tuple, expected_tuple = params_get_results
    test_name, test_list = input_tuple
    result_tuple = get_results(test_name, test_list)
    assert result_tuple == expected_tuple


def test_get_results_empty_list():
    with pytest.raises(StatisticsError):
        get_results("name", [])
