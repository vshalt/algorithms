"""
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE

pale, pale   -> true
pales, pale -> true
pale, bale  -> true
pale, bake  -> false
"""

def one_away(s1: str, s2: str) -> bool:
    def check_replace(a: str, b: str) -> bool:
        replaced = False
        for i in range(len(a)):
            if a[i] != b[i]:
                if replaced:
                    return False
                replaced = True
        return True

    def check_insert(a: str, b: str) -> bool:
        i, j = 0, 0
        inserted = False
        while i< len(a) and j< len(b):
            if a[i] != b[i]:
                if inserted:
                    return False
                inserted = True
                j += 1
            else:
                i += 1
                j += 1
        return True

    if len(s1) == len(s2):
        return check_replace(s1, s2)
    elif len(s1) - len(s2) == -1:
        return check_insert(s1, s2)
    elif len(s1) - len(s2) == 1:
        return check_insert(s2, s1)
    else:
        return False
