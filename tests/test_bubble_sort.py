from model.algos.bubble_sort import bubble_sort


def test_bubble_sort(input_expected):
    input_list, expected_list = input_expected
    result_list = bubble_sort(input_list)
    assert result_list == expected_list
    assert input_list is not result_list
