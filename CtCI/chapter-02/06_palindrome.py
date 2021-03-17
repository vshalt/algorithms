"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""
from linked_list import LinkedList
def palindrome(ll: LinkedList) -> bool:
    stack = []
    cursor = runner = ll.head
    while runner:
        stack.append(cursor._element)
        cursor = cursor._next
        runner = runner._next._next
    while cursor:
        out = stack.pop()
        if out != cursor._element:
            return False
        cursor = cursor._next
    return True
