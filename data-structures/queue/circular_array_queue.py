class Empty(Exception):
    """
    Raise exception when queue is empty
    """
    pass

class Queue():
    """
    Implementation of queue using circular lists
    Time complexities of class functions:
    func: __len__()     => O(1)
    func: is_empty()    => O(1)
    func: first()       => O(1)
    func: dequeue()     => O(1)
    func: enqueue()     => O(1)
    """
    CAPACITY = 10

    def __init__(self):
        self._queue = [None] * Queue.CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        Return len of queue
        """
        return self._size

    def __str__(self):
        return str(self._queue)

    def __repr__(self):
        return self.__str__()

    def is_empty(self):
        """
        Boolean value to represent if queue is empty
        """
        return self._size == 0

    def first(self):
        """
        Returns the first element that was enqueued into the queue
        The element which will be returned if dequeue() is called
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._queue[self._front]

    def dequeue(self):
        """
        Returns the first element that was enqueued into the queue.
        The element is removed from the queue.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % self._size
        self._size -= 1
        return answer

    def enqueue(self, element):
        """
        Adds an element to the end of queue. Resizes if necessary
        """
        if self._size == len(self._queue):
            self._resize(2 * self._size)
        available = (self._front + self._size) % len(self._queue)
        self._queue[available] = element
        self._size += 1

    def _resize(self, capacity):
        """
        Resize the queue with a new capacity if the queue if full
        """
        old = self._queue
        self._queue = [None] * capacity
        old_front = self._front
        for i in range(self._size):
            self._queue[i] = old[old_front]
            old_front = (1 + old_front) % len(old)
        self._front = 0
