# Algo quick sort (ou tri rapide)
# divided and conquered
import random

def quick_sort(input_list: list):
    copy_list = input_list.copy()
    first = 0
    last = len(copy_list) - 1

    def logic(input_list: list, first:int, last:int) -> list:
        if first < last:
            pivot:int = choose_pivot(input_list, first, last)
            pivot:int = partition(input_list, first, last, pivot)
            logic(input_list, first, pivot-1)
            logic(input_list, pivot+1, last)

    logic(copy_list, first, last)
    
    return copy_list

def choose_pivot(input_list: list, first:int, last:int)-> int:
    return random.randrange(first, last)

def partition(input_list: list, first:int, last:int, pivot: int)-> int:
    input_list[last], input_list[pivot] = input_list[pivot], input_list[last]
    j = first
    for i in range(first, last):
        if input_list[i] <=input_list[last]:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            j += 1
    input_list[last], input_list[j] = input_list[j], input_list[last]
    
    return j
    

# list_test = [3,5,2,1,8,7,9]
# sort_list = merge_sort(list_test)
# print(sort_list)