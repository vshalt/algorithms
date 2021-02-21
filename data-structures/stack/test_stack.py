import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(5)
        self.stack.push(4)

    def tearDowm(self):
        del self.stack

    def test_push(self):
        self.stack.push(9)
        self.stack.push(9)
        self.stack.push(9)
        self.assertEqual(str(self.stack), str([1, 2, 3, 5, 4, 9, 9, 9]))

    def test_pop(self):
        self.stack.pop()
        self.assertEqual(str(self.stack), str([1, 2, 3, 5]))
        temp = self.stack.pop()
        self.assertEqual(temp, 5)

    def test_top(self):
        temp = self.stack.top()
        self.assertEqual(temp, 4)
        self.stack.push(7)
        temp = self.stack.top()
        self.assertEqual(temp, 7)

    def test_length(self):
        temp = len(self.stack)
        self.assertEqual(temp, 5)
        self.stack.push(7)
        temp = len(self.stack)
        self.assertEqual(temp, 6)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), False)
        self.stack = Stack()
        self.assertEqual(self.stack.is_empty(), True)

if __name__ == '__main__':
    unittest.main()
