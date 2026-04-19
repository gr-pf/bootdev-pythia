from model.algos.selection_sort import selection_sort


def test_buildin_sort(input_expected):
    input_list, expected_list = input_expected
    assert selection_sort(input_list) == expected_list
