# Algo bubble sort (on fixe le max à chaque passage)
# Raw and optimised (si on ne modifie pas le tableau lors d'une boucle c'est qu'il est déjà trié)


def bubble_sort_raw(input_list: list):
    copy_list = input_list.copy()

    for i in range(len(copy_list) - 1, 0, -1):
        for j in range(0, i):
            if copy_list[j + 1] < copy_list[j]:
                copy_list[j + 1], copy_list[j] = copy_list[j], copy_list[j + 1]

    return copy_list


print(bubble_sort_raw([4, 3, 2, 1, 0]))


def bubble_sort_optimised(input_list: list):
    copy_list = input_list.copy()

    for i in range(len(copy_list) - 1, 0, -1):
        list_sorted = True
        for j in range(0, i):
            if copy_list[j + 1] < copy_list[j]:
                copy_list[j + 1], copy_list[j] = copy_list[j], copy_list[j + 1]
                list_sorted = False
        if list_sorted:
            return copy_list

    return copy_list
