class Tuple():
    """
    Tuple data type implemented in python.
        Time complexities of class functions:
        func: __len__()         => O(1)
        func: __getitem__()     => O(1)
        func: __setitem__()     => O(1)
        func: count()           => O(n)
        func: index_of()        => O(n)
    """
    def __init__(self, *args):
        """
        Initialize the tuple with the arguments as elements of the tuple
        """
        self.tuple = self._create_tuple(*args)
        self.length = len(args)

    def __getitem__(self, index):
        """
        Get item from tuple
        """
        return self.tuple[index]

    def __setitem__(self, index, element):
        """
        Set item to tuple
        """
        if index < 0 or index >= self.length:
            raise IndexError('Index out of bounds!')
        self.tuple[index] = element

    def _create_tuple(self, *args):
        """
        Private method to create a tuple
        """
        return [*args]

    def __str__(self):
        """
        String representation of tuple for print statements
        func: str()
        """
        temp = ""
        for i in range(self.length):
            if i == self.length -1:
                temp += str(self.tuple[i])
            else:
                temp += str(self.tuple[i]) + ", "
        return f"({temp})"

    def __repr__(self):
        """
        Representation of tuple for python interactive console
        func: repr()
        """
        return self.__str__()

    def __len__(self):
        """
        Returns length of tuple
        func: len()
        """
        return self.length

    def count(self, element):
        """
        Counts the number of times `element` in the tuple
        """
        if self.length == 0:
            raise ValueError('Tuple is empty')
        c = 0
        for i in range(self.length):
            if element == self.tuple[i]:
                c += 1
        return c

    def index_of(self, element):
        """
        Returns the index of `element` if it is in the tuple
        """
        if self.length == 0:
            raise ValueError('Tuple is empty')
        for i in range(self.length):
            if element == self.tuple[i]:
                return i
        return None
