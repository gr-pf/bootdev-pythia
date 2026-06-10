from model.algos.quick_sort import quick_sort


def test_quick_sort(input_expected):
    input_list, expected_list = input_expected
    result_list = quick_sort(input_list)
    assert result_list == expected_list
    assert input_list is not result_list