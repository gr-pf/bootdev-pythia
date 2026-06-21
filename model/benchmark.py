import random
import time
from collections.abc import Callable

from model.algos.liste_algos import list_algos


def generate_unsorted_list(n: int) -> list[int]:
    return random.sample(range(n), k=n)


def get_sorting_time_ms(size: int, algo: Callable[list[int]]) -> int:
    unsorted_list = generate_unsorted_list(size)
    start = time.time_ns()
    algo(unsorted_list)
    end = time.time_ns()
    return (end - start) / 1000000


def benchmark(algos: list, iter: int, size: int) -> list:
    results = []
    pass


print(get_sorting_time_ms(1000, list_algos[0].function))
