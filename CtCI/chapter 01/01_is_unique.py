"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

def is_unique(string: str) -> bool:
    max_non_repeating_chars = 128  # in case of ascii, 256 for extended ascii
    if len(string) > max_non_repeating_chars:
        return False

    char_map = [False] * 128
    for char in string:
        value = ord(char)
        if char_map[value]:
            return False
        char_map[value] = True
    return True
