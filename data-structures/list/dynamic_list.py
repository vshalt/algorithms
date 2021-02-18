import ctypes

class List():
    """
    List data type implemented in python.
    Item assignment not supported (arr[x] = y)
    """
    def __init__(self):
        """
        Initialize each list with the following parameters.
        """
        self.length = 0
        self.capacity = 1
        self.array = self._create_array(self.capacity)

    def __str__(self):
        """
        String representation of the list when using print()
        func: str()
        """
        temp = ""
        for i in range(self.length):
            if i == self.length -1:
                temp += str(self.array[i])
            else:
                temp += str(self.array[i]) + ", "
        return f'[{temp}]'

    def __repr__(self):
        """
        Representation of list in python interactive console
        func: repr()
        """
        return self.__str__()

    def __len__(self):
        """
        Returns length of the list.
        func: len()
        """
        return self.length

    def change(self, index, element):
        """
        Change the element at `index` to new `element`.
        """
        if self.length == 0:
            raise IndexError('List is empty')
        if index < 0 or index > self.length:
            raise IndexError('Index out of bounds!')
        self.array[index] = element

    def append(self, element):
        """
        Appends `element` to the list.
        """
        if self.length == self.capacity:
            self._resize_array(2 * self.capacity)
        self.array[self.length] = element
        self.length += 1

    def insert_at(self, index, element):
        """
        Inserts an element at the specified index.
        """
        if index < 0 or index > self.length:
            raise IndexError('Index out of bounds!')
        if index == self.length:
            self._resize_array(2 * self.capacity)
        if index == 0:
            for i in range(self.length):
                self.array[i + 1] = self.array[i]
        else:
            for i in range(index-1, self.length):
                self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.length += 1

    def pop(self):
        """
        Removes the last element from the list if the list is not empty.
        """
        if self.length == 0:
            raise IndexError('Cannot pop from null array')
        temp = self.array[self.length]
        self.array[self.length -1] = 0
        self.length -= 1
        return temp

    def clear(self):
        """
        Clears the list back to the initial state.
        """
        self.__init__()

    def index_of(self, element):
        """
        Returns the index of the `element` if it is present in the list.
        """
        for i in range(self.length):
            if self.array[i] == element:
                return i
        return None

    def contains(self, element):
        """
        Returns True if `element` is in the list else False.
        """
        return True if self.index_of(element) else False

    def count(self, element):
        """
        Returns number of times an `element` is present in the list.
        """
        c = 0
        for i in range(self.length):
            if self.array[i] == element:
                c += 1
        return c

    def remove_at(self, index):
        """
        Remove the element at the specified `index`.
        """
        if index < 0 or index > self.length:
            raise IndexError('Index out of bounds!')
        if self.length == 0:
            raise IndexError('Cannot remove from null array')
        for i in range(index, self.length):
            self.array[i] = self.array[i + 1]
        self.array[self.length] = 0
        self.length -= 1

    def remove(self, element):
        """
        Removes the first instance of `element` from the list.
        """
        index = self.index_of(element)
        if index:
            self.remove_at(index)
        else:
            raise ValueError('Element is not in the list')

    def reverse(self):
        """
        Reverses the list in place.
        """
        pointer = self.length - 1
        for i in range(self.length):
            if pointer > i:
                temp = self.array[i]
                self.array[i] = self.array[pointer]
                self.array[pointer] = temp
                pointer -= 1


    def _create_array(self, capacity):
        """
        Private method to create null slots in memory for array.
        Similar to int list[x] in C.
        """
        return (capacity * ctypes.py_object)()

    def _resize_array(self, new_capacity):
        """
        Private method create a new array with a `new_capacity` and copies all the content
        of the array into the new array
        """
        new_array = self._create_array(new_capacity)
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
