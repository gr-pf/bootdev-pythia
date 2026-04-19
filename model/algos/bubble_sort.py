# Algo bubble sort (on fixe le max à chaque passage)


def bubble_sort(input_list: list):
    copy_list = input_list.copy()
    swapping = True
    end = len(copy_list)

    while swapping:
        swapping = False
        for i in range(1, end):
            if copy_list[i - 1] > copy_list[i]:
                copy_list[i - 1], copy_list[i] = copy_list[i], copy_list[i - 1]
                swapping = True
        end -= 1

    return copy_list
