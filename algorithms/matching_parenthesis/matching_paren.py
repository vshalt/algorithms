"""
Algorithm to find if the parenthesis are equal and correctly closed in a given string

'(({[]}))'  => True
'()[]{}'    => True
'(()))[['   => False
"""

def matching_paren(string):
    """
    Implementation using stacks
    """
    left = '([{'
    right = ')]}'
    stack = []
    for char in string:
        if char in left:
            stack.append(char)
        elif char in right:
            if len(stack) == 0:
                return False
            if right.index(char) != left.index(stack.pop()):
                return False
    return stack == []
