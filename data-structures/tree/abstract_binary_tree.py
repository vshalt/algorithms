from abstract_tree import Tree

class BinaryTree(Tree):
    """
    Abstract class representing binary tree
    """
    def left(self, position):
        raise NotImplementedError('Must be implemented by subclass')

    def right(self, position):
        raise NotImplementedError('Must be implemented by subclass')

    def sibling(self, position):
        parent = self.parent(position)
        if parent is None:
            return None
        else:
            if position == self.left(parent):
                return self.right(parent)
            if position == self.right(parent):
                return self.left(parent)

    def children(self, position):
        if self.left(position) is not None:
            yield self.left(position)
        if self.right(position) is not None:
            yield self.right(position)

