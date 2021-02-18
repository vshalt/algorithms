import unittest
from dynamic_list import List

class TestList(unittest.TestCase):
    def setUp(self):
        arr = List()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        arr.append(4)
        self.arr = arr

    def tearDown(self):
        self.arr = List()

    def test_append(self):
        self.arr.append(10)
        self.assertEqual(str(self.arr), str([1, 2, 3, 4, 10]))

    def test_clear(self):
        self.arr.clear()
        self.assertEqual(str(self.arr), str([]))

    def test_insert_at(self):
        self.arr.insert_at(1, 10)
        self.assertEqual(str(self.arr), str([1, 10, 2, 3, 4]))

    def test_pop(self):
        self.arr.pop()
        self.assertEqual(str(self.arr), str([1, 2, 3]))

    def test_remove(self):
        self.arr.remove(2)
        self.assertEqual(str(self.arr), str([1, 3, 4]))

    def test_contains(self):
        self.assertEqual(self.arr.contains(3), True)
        self.assertEqual(self.arr.contains(13), False)

    def test_count(self):
        self.assertEqual(self.arr.count(1), 1)
        self.assertEqual(self.arr.count(2), 1)
        self.assertEqual(self.arr.count(12), 0)

    def test_index_of(self):
        self.assertEqual(self.arr.index_of(2), 1)
        self.assertEqual(self.arr.index_of(12), None)

    def test_remove_at(self):
        self.arr.remove_at(3)
        self.assertEqual(str(self.arr), str([1, 2, 3]))
        with self.assertRaises(IndexError):
            self.arr.remove_at(5)

    def test_reverse(self):
        self.arr.reverse()
        self.assertEqual(str(self.arr), str([4, 3, 2, 1]))

    def test_change(self):
        self.arr.change(1, 5)
        self.assertEqual(str(self.arr), str([1, 5, 3, 4]))

    def test_len(self):
        self.assertEqual(len(self.arr), 4)

if __name__ == '__main__':
    unittest.main()
