from model.algos.buildin_sorted import buildin_sorted


def test_buildin_sorted(input_expected):
    input_list, expected_list = input_expected
    result_list = buildin_sorted(input_list)
    assert result_list == expected_list
    assert input_list is not result_list
