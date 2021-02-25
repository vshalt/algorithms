class Empty(Exception):
    """
    Exception to be raised when stack is empty
    """
    pass


class Stack():
    """
    Implementation of stack with singly linked list
    Time complexities of various class functions
    func: __len__()     => O(1)
    func: push()        => O(1)
    func: pop()         => O(1)
    func: top()         => O(1)
    func: is_empty()    => O(1)
    func: __str__()     => O(n)
    """
    class _Node():
        """
        Simplistic singly linked list node
        """
        __slots__ = '_next', '_element'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        """
        Returns length of the stack
        """
        return self._size

    def is_empty(self):
        """
        Boolean value to represent if stack is empty
        """
        return self._size == 0

    def push(self, element):
        """
        Push an element to the head of the stack
        """
        self._head = self._Node(element, self._head)
        self._size += 1

    def pop(self):
        """
        Remove an element from the head of the stack
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def top(self):
        """
        The latest pushed element is returned
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def __str__(self):
        """
        String representation of stack
        """
        node = self._head
        result = []
        while node:
            result.append(node._element)
            node = node._next
        result.reverse()
        return str(result)

    def __repr__(self):
        return self.__str__()

