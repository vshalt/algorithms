class Empty(Exception):
    """
    Raise this exception when stack is empty
    """
    pass

class Stack():
    """
    Implementation of Stack with lists.
    """
    def __init__(self, *args):
        """
        If args initialize the stack with the args
        """
        if args:
            self._stack = [*args]
        else:
            self._stack = []

    def __len__(self):
        """
        Returns length of the stack
        """
        return len(self._stack)

    def __str__(self):
        return str(self._stack)

    def __repr__(self):
        return self.__str__()

    def push(self, element):
        """
        Push an element to the end of the stack
        """
        self._stack.append(element)

    def pop(self):
        """
        Pop an element from the stack
        """
        if self.is_empty():
            raise Empty('Stack is empty, cannot pop from empty stack')
        else:
            element = self._stack.pop()
            return element

    def is_empty(self):
        """
        Returns boolean value to represent if the stack is emtpy
        """
        return len(self._stack) == 0

    def top(self):
        """
        Returns the top most pushed value in the stack.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            return self._stack[-1]
