"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Taco cat
Output: True (permutations: "taco cat", "atco eta", etc.)
"""
from collections import Counter

def palindrome_permutation(string: str) -> bool:
    ref = {}
    for char in string:
        if char == " ":
            continue
        ref[char] = ref.get(char, 0) + 1
    odd = False  # max only one odd pair is possible in the string
    for value in ref.values():
        if value % 2 == 1:
            if odd:
                return False
            odd = True
    return True


def palindrome_permutation_pythonic(string: str) -> bool:
    """
    since only one odd is possible, sum can never cross 1
    """
    ref = Counter(string)
    return sum(value % 2 for value in ref.values()) <= 1
