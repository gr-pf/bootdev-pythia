from model.algos.selection_sort import selection_sort


def test_selection_sort(input_expected):
    input_list, expected_list = input_expected
    result_list = selection_sort(input_list)
    assert result_list == expected_list
    assert input_list is not result_list
