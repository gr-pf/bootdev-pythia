# Algo selection sort
# Comme bubble sort met check uniquement le minimum à chaque boucle


def selection_sort(input_list: list):
    copy_list = input_list.copy()

    for i in range(len(copy_list)):
        index_minimum = i
        for j in range(i + 1, len(copy_list)):
            if copy_list[j] < copy_list[index_minimum]:
                index_minimum = j
        copy_list[i], copy_list[index_minimum] = copy_list[index_minimum], copy_list[i]

    return copy_list
