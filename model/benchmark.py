import random
import time
import statistics
from collections import namedtuple
from collections.abc import Callable

from model.algos.liste_algos import list_algos

TimesResult = namedtuple(
    "TimesResult", ["algo_name", "mean", "median", "min", "max", "variance"]
)


def generate_unsorted_list(n: int) -> list[int]:
    return random.sample(range(n), k=n)


def get_sorting_time_ms(size: int, algo: Callable[list[int]]) -> int:
    unsorted_list = generate_unsorted_list(size)
    start = time.time_ns()
    algo(unsorted_list)
    end = time.time_ns()
    return (end - start) / 1000000  # return in milliseconds


def get_results(algo: str, times: list[int]) -> TimesResult:
    if len(times) == 1:
        stat = times[0]
        return TimesResult(algo, stat, stat, stat, stat, 0)
    stat_mean = round(statistics.mean(times), 2)
    stat_median = round(statistics.median(times), 2)
    stat_min = round(min(times), 2)
    stat_max = round(max(times), 2)
    stat_variance = round(statistics.variance(times), 2)
    return TimesResult(algo, stat_mean, stat_median, stat_min, stat_max, stat_variance)


def benchmark(algos: list, iter: int, size: int) -> list:
    results = []

    for algo in algos:
        times = []
        for _ in range(iter):
            times.append(get_sorting_time_ms(size, list_algos[algo]))
        current_result = get_results(algo, times)
    pass


# print(get_sorting_time_ms(1000, list_algos["buildin_sort"].function))
# print(get_results("buildin_sort", []))
# print(get_results("buildin_sort", [12.5, 65, 45.2, 58, 59, 45.3]).variance)
