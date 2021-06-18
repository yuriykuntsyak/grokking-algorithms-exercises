import logging
import time

def get_exec_time(func, **kwargs):
    """
    Measures func() execution time.
    Returns func()'s return value.
    """

    start_time = time.perf_counter()
    return_val = func(**kwargs)
    exec_time = time.perf_counter() - start_time

    logging.debug(f"get_exec_time: {func.__name__} took {exec_time} seconds.")

    return return_val
