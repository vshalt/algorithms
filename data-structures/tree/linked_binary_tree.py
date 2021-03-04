from abstract_binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    class _Node():
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError('position is not of the Position class')
        if position._container is not self:
            raise ValueError('position does not belong to this container')
        if position._node._parent is position._node:
            raise ValueError('Position is no longer valid')
        return position._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, position):
        node = self._validate(position)
        return self._make_position(node._parent)

    def left(self, position):
        node = self._validate(position)
        return self._make_position(node._left)

    def right(self, position):
        node = self._validate(position)
        return self._make_position(node._right)

    def num_children(self, position):
        node = self._validate(position)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, element):
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(element)
        self._size = 1
        return self._make_position(self._root)

    def _add_left(self, position, element):
        node = self._validate(position)
        if node._left is not None:
            raise ValueError('Left branch exists')
        self._size += 1
        node._left = self._Node(element,node)
        return self._make_position(node._left)

    def _add_right(self, position, element):
        node = self._validate(position)
        if node._right is not None:
            raise ValueError('Right branch exists')
        self._size += 1
        node._right = self._Node(element, node)
        return self._make_position(node._right)

    def _replace(self, position, element):
        node = self._validate(position)
        old = node._element
        node._element = element
        return old

    def _delete(self, position):
        node = self._validate(position)
        if node.num_children(position) == 2:
            raise ValueError('Position has 2 children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if parent._left is node:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node   # garbage
        return node._element

    def _attach(self, position, tree_left, tree_right):
        node = self._validate(position)
        if not self.is_leaf(position):
            raise ValueError('Position must be a leaf')
        if not type(self) is type(tree_left) is type(tree_right):
            raise TypeError('Type must match')
        self._size += len(tree_left) + len(tree_right)
        if not tree_left.is_empty():
            tree_left._root._parent = node
            node._left = tree_left._root
            tree_left._root = None
            tree_left._size = 0
        if not tree_right.is_empty():
            tree_right._root._parent = node
            node._right = tree_right._root
            tree_right._root = None
            tree_right._size = 0
