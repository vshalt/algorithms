from abstract_map import MapBase

class UnsortedTableMap(MapBase):
    """
    Map implemented with list
    """
    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        for item in self._table:
            if item._key == key:
                return item._value
        raise KeyError('KeyError: ' + repr(key))

    def __setitem__(self, key, value):
        for item in self._table:
            if item._key == key:
                item._value = value
                return
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        for i in range(len(self._table)):
            if key == self._table[i]._key:
                self._table.pop(i)
                return
        raise KeyError('KeyError: ' + repr(key))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key

