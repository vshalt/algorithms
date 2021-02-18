import unittest
from tuple import Tuple

class TestTuple(unittest.TestCase):
    def setUp(self):
        self.tuple = Tuple(1, 2, 3, 4, 5)

    def tearDown(self):
        self.tuple = Tuple()

    def test_len(self):
        self.assertEqual(len(self.tuple), 5)

    def test_change(self):
        with self.assertRaises(IndexError):
            self.tuple.change(19, 5)
        self.tuple.change(1, 10)
        self.assertEqual(str(self.tuple), str((1, 10, 3, 4, 5)))

    def test_count(self):
        self.assertEqual(self.tuple.count(1), 1)
        self.assertEqual(self.tuple.count(15), 0)

    def test_index_of(self):
        self.assertEqual(self.tuple.index_of(1), 0)
        self.assertEqual(self.tuple.index_of(2), 1)
        self.assertEqual(self.tuple.index_of(3), 2)
        self.assertEqual(self.tuple.index_of(4), 3)
        self.assertEqual(self.tuple.index_of(5), 4)

if __name__ == '__main__':
    unittest.main()
