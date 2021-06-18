#!/usr/bin/env python3

import logging
import os
import random

from algorithms import binary_search
from test_cases import ordered_int_array
from utils import get_exec_time

logging.basicConfig(
    level=int(
        os.getenv("LOGLEVEL", default=logging.INFO)
    )
)

def main():
    item = int(os.getenv(
        "ITEM", 
        default=random.randint(0,len(ordered_int_array))
    ))

    get_exec_time(
        binary_search,
        list=ordered_int_array,
        item=item
    )

if __name__ == '__main__':
    main()
