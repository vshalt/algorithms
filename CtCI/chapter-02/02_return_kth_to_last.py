"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
from linked_list import LinkedList

def return_kth_to_last(linked_list: LinkedList, k: int) -> LinkedList:
    cursor = runner = linked_list.head
    for _ in range(k):
        if not runner:
            return None
        runner = runner._next

    while runner:
        cursor = cursor._next
        runner = runner._next
    return cursor
