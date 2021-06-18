#!/usr/bin/env python3

import logging
import os
import time

logging.basicConfig(
    level=int(
        os.getenv("LOGLEVEL", default=logging.INFO)
    )
)

DEFAULT_MAX_LEN = 100
MAX_LEN = int(os.getenv("MAX_LEN", default=DEFAULT_MAX_LEN))
ordered_int_array = []

def generate_ordered_array(array, len):
    for i in range(0,len):
        array.append(i)

if __name__ == 'test_cases':
    startTime = time.perf_counter()
    
    generate_ordered_array(ordered_int_array, MAX_LEN)

    logging.debug(
        f"test_cases: Generated array of {MAX_LEN} integers in {time.perf_counter() - startTime} seconds."
    )
