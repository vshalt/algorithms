"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 0s digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7->1->6) + (5->9->2).That is,617 + 295.
Output: 2->1->9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6->1->7) + (2->9->5).That is, 617 + 295,
Output:9->1->2,That is,912.
"""
from linked_list import LinkedList

def sum_lists(ll1: LinkedList, ll2: LinkedList):
    a = ll1.head
    b = ll2.head
    out = LinkedList()
    carry = 0
    while a or b:
        sum = carry
        if a:
            sum += a._element
            a = a._next
        if b:
            sum += b._element
            b = b._next
        out.insert(sum % 10)
        carry = sum // 10
    if carry:
        out.insert(carry)
    return out

def sum_lists_followup(ll1: LinkedList, ll2:LinkedList):
    len_diff = len(ll1) - len(ll2)
    if len_diff < 0:
        pad_zeroes(ll1, abs(len_diff))
    elif len_diff > 0:
        pad_zeroes(ll2, len_diff)
    result, carry = recursive_sum(ll1.head, ll2.head)
    if carry:
        node = LinkedList._Node(1, result)
        return node
    return result

# helper function for sum_lists_followup
def recursive_sum(ll1, ll2):
    if ll1 is None and ll2 is None:
        return None, 0
    res, carry = recursive_sum(ll1._next, ll2._next)
    val = ll1._element + ll2._element + carry
    node = LinkedList._Node(val % 10, res)
    return node, val // 10

# helper function for sum_lists_followup
def pad_zeroes(ll: LinkedList, diff: int):
    for _ in range(diff):
        node = LinkedList._Node(0, ll.head)
        ll.head = node
