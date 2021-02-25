import unittest
from circular_array_stack import Stack as CircularStack
from linked_list_stack import Stack as LinkedListStack

class TestCircularStack(unittest.TestCase):
    def setUp(self):
        self.stack = CircularStack()
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
        self.stack = CircularStack()
        self.assertEqual(self.stack.is_empty(), True)

class TestLinkedListStack(unittest.TestCase):
    def setUp(self):
        self.stack = LinkedListStack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(5)
        self.stack.push(4)

    def test_push(self):
        TestCircularStack.test_push(self)

    def test_pop(self):
        TestCircularStack.test_pop(self)

    def test_top(self):
        TestCircularStack.test_top(self)

    def test_length(self):
        TestCircularStack.test_length(self)

    def test_is_empty(self):
        self.assertEqual(self.stack._head is None, False)
        self.stack = LinkedListStack()
        self.assertEqual(self.stack._head == None, True)

if __name__ == '__main__':
    unittest.main()
