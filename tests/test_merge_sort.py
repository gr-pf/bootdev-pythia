from model.algos.merge_sort import merge_sort


def test_merge_sort(input_expected):
    input_list, expected_list = input_expected
    result_list = merge_sort(input_list)
    assert result_list == expected_list
    assert input_list is not result_list
