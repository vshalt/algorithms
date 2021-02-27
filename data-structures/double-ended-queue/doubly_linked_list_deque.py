class Empty(Exception):
    pass

class DoublyLinkedList():
    """
    Doubly linked list implemented
    """
    class _Node():
        """
        Simplistic doubly linked list node
        """
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """
        Returns length of linked list
        """
        return self._size

    def is_empty(self):
        """
        Boolean value to represent if linked list is empty
        """
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        """
        Insert a node between 2 nodes
        """
        new_node = self._Node(element, predecessor, successor)
        predecessor._next = new_node
        successor._next = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """
        Delete a node from the list
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

class Deque(DoublyLinkedList):
    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def add_first(self, element):
        self._insert_between(element, self._header, self._header._next)

    def add_last(self, element):
        self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._trailer._prev)


