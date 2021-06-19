#!/usr/bin/env python3

import logging
import os

from algorithms import selection_sort
from test_cases import unordered_int_array
from utils import get_exec_time

logging.basicConfig(
    level=int(
        os.getenv("LOGLEVEL", default=logging.INFO)
    )
)

def main():
    sorted_array = get_exec_time(
        selection_sort,
        array=unordered_int_array
    )

if __name__ == '__main__':
    main()
