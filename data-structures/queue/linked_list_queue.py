class Empty(Exception):
    """
    Exception to be raised when queue is empty
    """
    pass

class Queue():
    """
    Implementation of queue with singly linked list
    Time complexities of the class functions:
    func: __len__()     => O(1)
    func: is_empty()    => O(1)
    func: enqueue()     => O(1)
    func: dequeue()     => O(1)
    func: first()       => O(1)
    func: __str__()     => O(n)
    """
    class _Node():
        """
        Simplistic singly linked list
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        Returns length of the queue
        """
        return self._size

    def is_empty(self):
        """
        Boolean value to represent if queue is empty
        """
        return self._size == 0

    def enqueue(self, element):
        """
        Append elements to the end of the linked list
        """
        new_node = self._Node(element, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """
        Remove the head of the linked list
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def first(self):
        """
        Return the head of the linked list
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element


    def __str__(self):
        """
        String representation of the queue
        """
        result = []
        node = self._head
        while node:
            result.append(node._element)
            node = node._next
        return str(result)

    def __repr__(self):
        return self.__str__()
