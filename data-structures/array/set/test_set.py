import unittest
from set import Set

class TestSet(unittest.TestCase):
    def setUp(self):
        self.set = Set(1, 2, 3, 4, 4, 3, 5)

    def tearDown(self):
        self.set = Set()

    def test_len(self):
        self.assertEqual(len(self.set), 5)

    def test_add(self):
        self.set.add(5)
        self.set.add(4)
        self.set.add(6)
        self.assertEqual(str(self.set), str({1, 2, 3, 4, 5, 6}))

    def test_remove(self):
        self.set.remove(5)
        self.assertEqual(str(self.set), str({1, 2, 3, 4}))

    def test_pop(self):
        self.set.pop()
        self.assertEqual(str(self.set), str({1, 2, 3, 4}))

if __name__ == '__main__':
    unittest.main()
