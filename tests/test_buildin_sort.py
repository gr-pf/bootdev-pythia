from model.algos.buildin_sort import buildin_sort


def test_buildin_sort(input_expected):
    input_list, expected_list = input_expected
    assert buildin_sort(input_list) == expected_list
