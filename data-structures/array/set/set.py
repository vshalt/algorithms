import collections

class Set():
    """
    Set implemented in python
    """
    def __init__(self, *args):
        if args:
            self.set = self._make_set(*args)
            self.length = len(self.set)
        else:
            self.set = self._make_empty_set()
            self.length = 0

    def __str__(self):
        temp = ""
        for i in range(self.length):
            temp += str(self.set[i])
            if i < self.length -1:
                temp += ", "
        return "{" + temp + "}"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.length

    def _make_set(self, *args):
        set = [*args]
        set = self._remove_duplicates(set)
        return set

    def _make_empty_set(self):
        return []

    def _remove_duplicates(self, set):
        temp = collections.Counter(set)
        return list(temp.keys())

    def add(self, element):
        if element not in self.set:
            self.set.append(element)
            self.length += 1

    def remove(self, element):
        if element in self.set:
            idx = self.set.index(element)
            for i in range(idx, self.length -1):
                self.set[i] = self.set[i + 1]
            self.set[self.length -1] = 0
            self.length -= 1

    def clear(self):
        self.__init__()

    def pop(self):
        if self.length == 0:
            raise IndexError('Cannot pop from empty set')
        temp = self.set[self.length - 1]
        self.set[self.length - 1] = 0
        self.length -= 1
        return temp
