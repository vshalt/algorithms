"""
Pseudocode for breadth first traversal

Algorithm breadthfirst(T):
    Initialize queue Q to contain T.root()
    while Q not empty do
    p = Q.dequeue()        {p is the oldest entry in the queue}
    perform the “visit” action for position p
    for each child c in T.children(p) do
    Q.enqueue(c)            {add p’s children to the end of the queue for later visits}
"""

import queue

def breadth_first(Tree):
    queue = queue.Queue()
    queue.put(Tree.root())
    while not queue.empty():
        position = queue.get()
        print(position.element())
        for child in Tree.children(position):
            queue.put(child)
