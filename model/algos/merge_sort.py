# Algo merge sort (ou tri par fusion)
# divided and conquered


def merge_sort(input_list: list):
    if len(input_list) < 2:
        return input_list

    middle = len(input_list) // 2

    left_side = merge_sort(input_list[:middle])
    right_side = merge_sort(input_list[middle:])

    return merge(left_side, right_side)


def merge(left: list, right: list):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    new_list = []
    l: int = 0  # noqa: E741
    r: int = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            new_list.append(left[l])
            l += 1  # noqa: E741
        else:
            new_list.append(right[r])
            r += 1

    while l < len(left):
        new_list.append(left[l])
        l += 1  # noqa: E741

    while r < len(right):
        new_list.append(right[r])
        r += 1

    return new_list
