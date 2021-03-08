"""
Pseudocode for postorder traversal

Algorithm postorder(T, p):
    for each child c in T.children(p) do
    postorder(T, c)
    perform the “visit” action for position p
"""

def postorder(Tree, position):
    for child in Tree.children(position):
        postorder(Tree, child)
    print(position.element())
