from collections import namedtuple

from model.algos.buildin_sort import buildin_sort
from model.algos.buildin_sorted import buildin_sorted
from model.algos.bubble_sort import bubble_sort_raw, bubble_sort_optimised
from model.algos.insertion_sort import insertion_sort
from model.algos.merge_sort import merge_sort
from model.algos.selection_sort import selection_sort
from model.algos.quick_sort import quick_sort

AlgoType = namedtuple("AlgoType", ["id", "name", "function"])
list_algos = [
    AlgoType("1", "Buildin sort", buildin_sort),
    AlgoType("2", "Buildin sorted", buildin_sorted),
    AlgoType("3", "Bubble sort", bubble_sort_raw),
    AlgoType("4", "Bubble sort optimisée", bubble_sort_optimised),
    AlgoType("5", "Insertion sort", insertion_sort),
    AlgoType("6", "Merge sort", merge_sort),
    AlgoType("7", "Selection sort", selection_sort),
    AlgoType("8", "Quick sort", quick_sort),
]
