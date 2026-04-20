from model.algos.buildin_sort import buildin_sort


def test_buildin_sort(input_expected):
    input_list, expected_list = input_expected
    result_list = buildin_sort(input_list)
    assert result_list == expected_list
    assert input_list is not result_list
