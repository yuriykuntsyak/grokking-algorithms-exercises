import logging
import os
import random

from utils import get_exec_time

logging.basicConfig(
    level=int(
        os.getenv("LOGLEVEL", default=logging.INFO)
    )
)

DEFAULT_MAX_LEN = 100
MAX_LEN = int(os.getenv("MAX_LEN", default=DEFAULT_MAX_LEN))
ordered_int_array = []
unordered_int_array = []

def generate_ordered_array(array, len):
    for i in range(0,len):
        array.append(i)

def generate_unordered_array(array, len):
    for i in range(0,len):
        array.append(random.randint(0,len))

if __name__ == 'test_cases':    
    get_exec_time(
        generate_ordered_array,
        array=ordered_int_array,
        len=MAX_LEN
    )

    get_exec_time(
        generate_unordered_array,
        array=unordered_int_array,
        len=MAX_LEN
    )

    logging.info(f"test_cases: Generated test cases.")
