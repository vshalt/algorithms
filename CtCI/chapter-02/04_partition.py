"""
Partition: Write code to partition a linked list around a value x,
such that all nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list, the values of x only need
to be after the elements less than x (see below).
The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3-> 5-> 8-> 5-> 10-> 2-> 1 [partition = 5]
Output: 3-> 1-> 2-> 10-> 5-> 5-> 8
"""
from linked_list import LinkedList, DoublyLinkedList

def partition(linked_list: LinkedList, pivot: int):
    a_head, a_tail, b_head, b_tail = None
    cursor = linked_list.head
    while cursor:
        if cursor._element < pivot:
            if a_head:
                a_tail = cursor
                a_tail._next = cursor
            else:
                a_head = cursor
                a_tail = cursor
        else:
            if b_head:
                b_tail = cursor
                b_tail._next = cursor
            else:
                b_tail = cursor
                b_head = cursor
        cursor = cursor._next
    a_tail._next = b_head
    return a_head


def partition_alt(linked_list: DoublyLinkedList, pivot: int):
    head, tail = LinkedList()
    head._next = tail
    cursor = linked_list.head
    while cursor:
        if cursor._element < pivot:
            cursor._next = head
            head = cursor
        else:
            tail._next = cursor
            tail = cursor
    tail._next = None
