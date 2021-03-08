"""
Pseudocode for preorder traversal

Algorithm preorder(T, p):
    perform the “visit” action for position p
    for each child c in T.children(p) do
    preorder(T, c)
"""

def preorder(Tree, position):
    yield position.element()
    for child in Tree.children(position):
        preorder(Tree, child)

