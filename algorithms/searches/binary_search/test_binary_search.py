import unittest
from binary_search import binary_search, recursive_binary_search

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def tearDowm(self):
        del self.array

    def test_binary_search(self):
        self.assertEqual(binary_search(self.array, 6), 5)
        self.assertEqual(binary_search(self.array, 1), 0)
        self.assertEqual(binary_search(self.array, 10), 9)
        self.assertEqual(binary_search(self.array, 15), -1)

    def test_recursive_binary_search(self):
        self.assertEqual(recursive_binary_search(self.array, 6, 0, 11), 5)
        self.assertEqual(recursive_binary_search(self.array, 1, 0, 11), 0)
        self.assertEqual(recursive_binary_search(self.array, 10, 0, 11), 9)
        self.assertEqual(recursive_binary_search(self.array, 15, 0, 11), -1)

if __name__ == '__main__':
    unittest.main()
