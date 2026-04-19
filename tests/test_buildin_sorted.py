from model.algos.buildin_sorted import buildin_sorted


def test_buildin_sort(input_expected):
    input_list, expected_list = input_expected
    assert buildin_sorted(input_list) == expected_list
