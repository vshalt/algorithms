class Empty(Exception):
    """
    Exception to raise when deque is empty
    """
    pass


class Deque():
    """
    Implementation of deque using circular arrays.
    """
    def __init__(self):
        self._capacity = 1
        self._deque = [None] * self._capacity
        self._size = 0
        self._front = 0
        self._rear = 0

    def __str__(self):
        """
        returns string representation of deque
        """
        return str(self._deque)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        """
        Returns length of the deque
        """
        return self._size

    def _resize(self, capacity):
        """
        Resize the deque with the new capacity
        """
        temp = [None] * capacity
        for i in range(self._capacity):
            temp[i] = self._deque[(self._front + i) % self._capacity]
        self._deque = temp
        self._front = 0
        self._rear = self._capacity -1
        self._capacity = capacity

    def add_front(self, element):
        """
        Append element to the front of the deque
        """
        if self._size == self._capacity:
            self._resize(self._size * 2)
        self._front = (self._front -1) % self._capacity
        self._deque[self._front] = element
        self._size += 1

    def add_rear(self, element):
        """
        Append elements to the rear of the deque
        """
        if self._size == self._capacity:
            self._resize(self._size * 2)
        self._rear = (self._rear + 1) % self._capacity
        self._deque[self._rear] = element
        self._size += 1

    def delete_front(self):
        """
        Delete the element that was in the first position in the deque
        """
        answer = self._deque[self._front]
        self._deque[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return answer

    def delete_rear(self):
        """
        Delete the element in the last position in the deque
        """
        answer = self._deque[self._rear]
        self._deque[self._rear] = None
        self._rear = (self._rear -1) % self._capacity
        self._size -= 1
        return answer

    def first(self):
        """
        Returns the first value in the deque
        """
        return self._deque[self._front]

    def rear(self):
        """
        Returns the last value in the deque
        """
        return self._deque[self._rear]

    def is_empty(self):
        """
        Boolean value to represent if the deque is empty
        """
        return self._size == 0
