import unittest
from linear_search import linear_search, recursive_linear_search

class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_linear_search(self):
        self.assertEqual(linear_search(self.array, 1), 0)
        self.assertEqual(linear_search(self.array, 2), 1)
        self.assertEqual(linear_search(self.array, 3), 2)
        self.assertEqual(linear_search(self.array, 4), 3)
        self.assertEqual(linear_search(self.array, 5), 4)
        self.assertEqual(linear_search(self.array, 6), 5)
        self.assertEqual(linear_search(self.array, 7), 6)
        self.assertEqual(linear_search(self.array, 8), 7)
        self.assertEqual(linear_search(self.array, 9), 8)
        self.assertEqual(linear_search(self.array, 11), -1)

    def test_recursive_linear_search(self):
        self.assertEqual(recursive_linear_search(self.array, 1, 9, 0), 0)
        self.assertEqual(recursive_linear_search(self.array, 2, 9, 0), 1)
        self.assertEqual(recursive_linear_search(self.array, 3, 9, 0), 2)
        self.assertEqual(recursive_linear_search(self.array, 4, 9, 0), 3)
        self.assertEqual(recursive_linear_search(self.array, 5, 9, 0), 4)
        self.assertEqual(recursive_linear_search(self.array, 6, 9, 0), 5)
        self.assertEqual(recursive_linear_search(self.array, 7, 9, 0), 6)
        self.assertEqual(recursive_linear_search(self.array, 8, 9, 0), 7)
        self.assertEqual(recursive_linear_search(self.array, 9, 9, 0), 8)
        self.assertEqual(recursive_linear_search(self.array, 11, 9, 0), -1)


if __name__ == '__main__':
    unittest.main()
