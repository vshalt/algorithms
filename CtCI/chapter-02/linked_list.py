class LinkedList():
    class _Node():
        __slots__ = '_element', '_next'

        def __init__(self,element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self.head = self._Node(None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def remove(self, element):
        if self._size == 0:
            raise Exception('Linked list is empty')
        cursor = self.head
        previous = None
        while cursor is not None:
            if cursor._element == element:
                previous = cursor
            cursor = cursor._next
        if previous:
            previous._next = cursor._next
            cursor._next = cursor._element = None
        return

    def insert(self, element):
        if self.head is None:
            node = self._Node(element, None)
        else:
            node = self._Node(element, self.head)
        self.head = node

class DoublyLinkedList():
    class _Node():
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self.head = self._Node(None, None, None)
        self.tail = self._Node(None, None, None)
        self.head._next = self.tail
        self.tail._prev = self.head
        self._size = 0

    def insert(self, element, predecessor, successor):
        node = self._Node(element, predecessor, successor)
        predecessor._next = node
        successor._prev = node

    def remove(self, element):
        cursor = self.head
        while cursor._element is not None:
            if cursor._element == element:
                prev = cursor._prev
                next = cursor._next
                prev._next = next
                next._prev = prev
                return
            cursor = cursor._next
        raise Exception('Element not in linkedlist')
