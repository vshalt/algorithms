import unittest
from circular_array_queue import Queue as CircularQueue
from circular_array_queue import Empty
from linked_list_queue import Queue as LinkedListQueue

class TestCircularQueue(unittest.TestCase):
    def setUp(self):
        self.queue = CircularQueue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.enqueue(7)
        self.queue.enqueue(8)
        self.queue.enqueue(9)

    def tearDown(self):
        del self.queue

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertEqual(str(self.queue), str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_dequeue(self):
        temp = self.queue.dequeue()
        self.assertEqual(temp, 1)
        self.assertEqual(str(self.queue),
                         str([None, 2, 3, 4, 5, 6, 7, 8, 9, None]))
        self.queue = CircularQueue()
        with self.assertRaises(Empty):
            self.queue.dequeue()

    def test_first(self):
        self.assertEqual(self.queue.first(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.first(), 2)
        self.queue = CircularQueue()
        with self.assertRaises(Empty):
            self.queue.first()


    def test_length(self):
        self.assertEqual(len(self.queue), 9)
        self.queue.enqueue(10)
        self.assertEqual(len(self.queue), 10)
        self.queue.enqueue(10)
        self.assertEqual(len(self.queue), 11)

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), False)
        self.queue = CircularQueue()
        self.assertEqual(self.queue.is_empty(), True)


class TestLinkedListQueue(unittest.TestCase):
    def setUp(self):
        self.queue = LinkedListQueue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), False)
        self.queue = LinkedListQueue()
        self.assertEqual(self.queue.is_empty(), True)

    def test_length(self):
        self.assertEqual(len(self.queue), 4)

    def test_enqueue(self):
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.assertEqual(str(self.queue), str([1, 2, 3, 4, 5, 6]))

    def test_dequeue(self):
        answer = self.queue.dequeue()
        self.assertEqual(str(self.queue), str([2, 3, 4]))
        self.assertEqual(answer, 1)

    def test_first(self):
        self.assertEqual(self.queue.first(), 1)


if __name__ == '__main__':
    unittest.main()
