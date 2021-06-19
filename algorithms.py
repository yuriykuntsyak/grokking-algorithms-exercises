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

def find_smallest_element(array) -> int:
    smallest_element_idx = 0

    for idx, element in enumerate(array):
        if array[smallest_element_idx] > element:
            smallest_element_idx = idx

    return smallest_element_idx

def selection_sort(array):
    sorted_array = []
    for idx, element in enumerate(array):
        smallest_idx = find_smallest_element(array)
        sorted_array.append(array.pop(smallest_idx))

    return sorted_array