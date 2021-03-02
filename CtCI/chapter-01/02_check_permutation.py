"""
Given two strings, write a method to decide if one is a permutation of the other.
"""
from collections import Counter

def check_permutation(s1: str, s2: str) -> bool:
    max_non_repeating_chars = 128  # in case of ascii, 256 for extended ascii
    if len(s1) != len(s2):
        return False
    char_map = [0] * max_non_repeating_chars
    for char in s1:
        char_map[ord(char)] += 1
    for char in s2:
        if char_map[ord(char)] == 0:
            return False
        char_map[ord(char)] -= 1
    return True

def check_permutation_pythonic(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)
