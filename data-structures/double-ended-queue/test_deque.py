import unittest
from deque import Deque

class TestDeque(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()
        self.deque.add_front(1)
        self.deque.add_front(2)

    def test_delete_front(self):
        answer = self.deque.delete_front()
        self.assertEqual(answer, 2)
        self.assertEqual(str(self.deque), str([1, None]))

    def test_delete_rear(self):
        answer = self.deque.delete_rear()
        self.assertEqual(answer, 1)
        self.assertEqual(str(self.deque), str([None, 2]))

    def test_add_front(self):
        self.deque.add_front(3)
        self.assertEqual(str(self.deque), str([2, 1, None, 3]))

    def test_add_rear(self):
        self.deque.add_rear(0)
        self.assertEqual(str(self.deque), str([2, 1, 0, None]))

    def test_front(self):
        self.assertEqual(self.deque.first(), 2)

    def test_rear(self):
        self.assertEqual(self.deque.rear(), 1)

    def test_is_emtpy(self):
        self.assertEqual(self.deque.is_empty(), False)
        self.deque = Deque()
        self.assertEqual(self.deque.is_empty(), True)

if __name__ == '__main__':
    unittest.main()
