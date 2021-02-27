from doubly_linked_list import DoublyLinkedList

class PositionalList(DoublyLinkedList):
    class Position():
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            return not(self == other)

    def _validate(self, position):
        if isinstance(position, self.Position):
            raise TypeError('Position is not of the proper position')
        if position._container is not self:
            raise ValueError('Position does not belong to this container')
        if position._node._next is None:
            raise ValueError('Position is not valid')
        return position._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, position):
        node = self._validate(position)
        return self._make_position(node._prev)

    def after(self, position):
        node = self._validate(position)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def insert_between(self, element, predecessor, successor):
        node = super().insert_between(element, predecessor, successor)
        return self._make_position(node)

    def add_first(self, element):
        node = super().insert_between(element, self._header, self._header._next)
        return self._make_position(node)

    def add_last(self, element):
        node = super().insert_between(element, self._trailer._prev, self._trailer)
        return self._make_position(node)

    def add_before(self, position, element):
        original = self._validate(position)
        return self.insert_between(element, original._prev, original)

    def add_after(self, position, element):
        original = self._validate(position)
        return self.insert_between(element, original, original._next)

    def delete(self, position):
        original = self._validate(position)
        return self.delete_node(original)

    def replace(self, position, element):
        original = self._validate(position)
        old_value = original._element
        original._element = element
        return old_value
