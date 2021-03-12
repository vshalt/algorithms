from collections.abc import MutableMapping
"""
MutableMapping implements all the dict class methods with the methods:
__getitem__, __setitem__, __len__, __delitem__, __iter__. These methods need to
be implemented in the children classes.
"""

class MapBase(MutableMapping):
    """
    Abstract base class to make maps
    """
    class _Item():
        """
        Non public class to group key, values
        """
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not(self == other)

        def __lt__(self, other):
            return self._key < other._key
