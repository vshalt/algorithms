class Tree():
    """
    Abstract base class to represent a tree
        (A)
        / \
      (B) (c)
      /|\   \
     / | \   (D)
  (E) (F) (G)
    """
    class Position():
        """
        Abstract class representing the position of an element
        """
        def element(self):
            """
            Returns the element at a position
            """
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            return not(self == other)

    def root(self):
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, position):
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, position):
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, position):
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('Must be implemented by subclass')

    def is_root(self, position):
        return self.root() == position

    def is_leaf(self, position):
        return self.num_children() == 0

    def is_empty(self):
        return self.__len__() == 0

    def depth(self, position):
        if self.is_root(position):
            return 0
        else:
            return 1 + self.depth(self.parent(position))

    def _height(self, position):
        if self.is_leaf(position):
            return 0
        else:
            return 1 + max(self._height(p) for p in self.children(position)))

    def height(self, position = None):
        if position is None:
            position = self.root()
        return self._height(position)
