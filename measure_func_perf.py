import tracemalloc
from time import perf_counter


def measure_func_perf(func):
    """Measure performance of a function"""

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f"Function: {func.__name__}")
        print(f"Memory usage:\t\t {current / 10**6:.6f} MB \n" f"Peak memory usage:\t {peak / 10**6:.6f} MB ")
        print(f"Time elapsed is seconds: {finish_time - start_time:.6f}")
        print(f'{"="*40}')
        tracemalloc.stop()

    return wrapper



# Usage:
@measure_func_perf
def create_list():
    my_list = [i**3 for i in range(1000000)]
    print(my_list[-1])
