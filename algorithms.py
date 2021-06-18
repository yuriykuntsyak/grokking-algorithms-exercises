import logging

def binary_search(list, item):
    low = 0
    high = len(list)-1

    logging.debug(f"binary_search: item: {item}.")

    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]

        logging.debug(f"binary_search: l: {low} - m: {mid} - h: {high}.")

        if guess == item:
            logging.debug(f"binary_search: found {item} at index {mid}.")
            return mid
        elif guess < item:
            low = mid+1
        else:
            high = mid-1

    logging.debug(f"binary_search: {item} not found.")

    return None