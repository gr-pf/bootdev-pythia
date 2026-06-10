# Algo quick sort (ou tri rapide)
# divided and conquered
import random

def quick_sort(input_list: list[int])-> list[int]:
    copy_list = input_list.copy()
    first = 0
    last = len(copy_list) - 1

    def logic(input_list: list[int], first:int, last:int):
        if first < last:
            pivot_index:int = choose_pivot(input_list, first, last)
            pivot_position:int = partition(input_list, first, last, pivot_index)
            logic(input_list, first, pivot_position-1)
            logic(input_list, pivot_position+1, last)

    logic(copy_list, first, last)
    
    return copy_list

def choose_pivot(input_list: list[int], first:int, last:int)-> int:
    return random.randint(first, last)

def partition(input_list: list[int], first:int, last:int, pivot: int)-> int:
    input_list[last], input_list[pivot] = input_list[pivot], input_list[last]
    j = first
    for i in range(first, last):
        if input_list[i] <=input_list[last]:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            j += 1
    input_list[last], input_list[j] = input_list[j], input_list[last]
    
    return j
