"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from linked_list import LinkedList

def remove_duplicates(linked_list: LinkedList) -> LinkedList:
    arr = []
    cursor = linked_list._header._next
    while cursor != linked_list._trailer:
        if cursor._element in arr:
            # cursor._next = cursor._next._next  # residual individual nodes
            temp = cursor._next
            linked_list.delete_node(cursor)
            cursor = temp
        else:
            arr.append(cursor._element)
            cursor = cursor._next
    return linked_list

def remove_duplicates_without_buffer(linked_list: LinkedList) -> LinkedList:
    cursor = linked_list._header._next
    while cursor != linked_list._trailer:
        runner = cursor
        while runner._next:
            if runner._next._element == cursor._element:
                # cursor._next = cursor._next._next  # residual individual nodes
                temp = cursor._next
                linked_list.delete_node(cursor)
                cursor = temp
            else:
                runner = runner._next
        cursor = cursor._next
    return linked_list

