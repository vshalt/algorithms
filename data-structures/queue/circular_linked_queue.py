class Empty(Exception):
    """
    Exception to be raised when queue is empty
    """
    pass

class Queue():
    """
    Implementation of queue using circular singly linked lists
    """
    class _Node():
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        result = []
        if self.is_empty():
            return str(result)
        node = self._tail._next
        result.append(node._element)
        node = node._next
        while node != self._tail._next:
            result.append(node._element)
            node = node._next
        return str(result)

    def __repr__(self):
        return self.__str__()

    def is_empty(self):
        """
        Boolean value to represent if the queue is empty
        """
        return self._size == 0

    def first(self):
        """
        Return the first element in the list
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def enqueue(self, element):
        """
        Add a new element to the end of the linked list
        """
        new_node = self._Node(element, None)
        if self.is_empty():
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """
        Remove the first added element
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        answer = head._element
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return answer

