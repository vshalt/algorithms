import unittest
from insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.array1 = [5, 4, 2, 6, 1, 2, 6, 19, 4, 3, 66]
        self.array2 = [5, 8, 7, 6, 1, 2, 9, 0, 4, 3, 10]

    def tearDown(self):
        del self.array1
        del self.array2

    def test_insertion_sort(self):
        insertion_sort(self.array1)
        self.assertEqual(self.array1, [1, 2, 2, 3, 4, 4, 5, 6, 6, 19, 66])
        insertion_sort(self.array2)
        self.assertEqual(self.array2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()
