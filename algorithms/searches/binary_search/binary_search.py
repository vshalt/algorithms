"""
Binary search algorithm implementation.
Returns -1 if target is not present in array, else sends the index of the target
The first function uses loop and the second function uses recursion.
"""
def binary_search(array, target):
    low = 0
    high = len(array) -1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

def recursive_binary_search(array, target, low, high):
    if low > high:
        return -1
    mid = (high + low) // 2
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return recursive_binary_search(array, target, low, mid-1)
    else:
        return recursive_binary_search(array, target, mid+1, high)
