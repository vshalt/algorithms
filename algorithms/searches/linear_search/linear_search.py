"""
Linear search algorithm implementation
Returns -1 if target is not present in array else returns the index of the element
"""
def linear_search(array, target):
    for index, item in enumerate(array):
        if item == target:
            return index
    return -1

def recursive_linear_search(array, target, high, low):
    if not(0 <= high < len(array) and 0 <= low < len(array)):
        raise Exception('Index out of bounds')
    if low > high:
        return -1
    if array[low] == target:
        return low
    if array[high] == target:
        return high
    return recursive_linear_search(array, target, high - 1, low + 1)

