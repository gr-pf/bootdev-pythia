from model.algos.bubble_sort import bubble_sort_raw, bubble_sort_optimised


def test_bubble_sort_raw(input_expected):
    input_list, expected_list = input_expected
    result_list = bubble_sort_raw(input_list)
    assert result_list == expected_list
    assert input_list is not result_list


def test_bubble_sort_optimised(input_expected):
    input_list, expected_list = input_expected
    result_list = bubble_sort_optimised(input_list)
    assert result_list == expected_list
    assert input_list is not result_list
