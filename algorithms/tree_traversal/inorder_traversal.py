"""
Pseudocode for inorder traversal
Algorithm inorder(p):
    if p has a left child lc then
    inorder(lc)                     {recursively traverse the left subtree of p}
    perform the “visit” action for position p
    if p has a right child rc then
    inorder(rc)
"""

def inorder(position):
    if position.left() != None:
        inorder(position.left())
    print(position.element())
    if position.right() != None:
        inorder(position.right())
