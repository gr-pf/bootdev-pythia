from model.algos.bubble_sort import bubble_sort


def test_buildin_sort(input_expected):
    input_list, expected_list = input_expected
    assert bubble_sort(input_list) == expected_list
