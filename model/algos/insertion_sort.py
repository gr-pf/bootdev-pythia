# Algo insertion sort
# On insére chaque élément à la "bonne place" dans un nouveau tableau


def insertion_sort(input_list: list):
    copy_list = input_list.copy()

    for i in range(1, len(copy_list)):
        tmp = copy_list[i]
        j = i
        while j > 0 and copy_list[j - 1] > tmp:
            copy_list[j] = copy_list[j - 1]
            j -= 1
        copy_list[j] = tmp

    return copy_list
