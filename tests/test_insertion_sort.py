from model.algos.insertion_sort import insertion_sort


def test_insertion_sort(input_expected):
    input_list, expected_list = input_expected
    result_list = insertion_sort(input_list)
    assert result_list == expected_list
    assert input_list is not result_list
