import unittest
from factorial import factorial, factorial_recursive

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_recursive_factorial(self):
        self.assertEqual(factorial_recursive(4), 24)
        self.assertEqual(factorial_recursive(3), 6)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(6), 720)
        self.assertEqual(factorial_recursive(7), 5040)
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(1), 1)

if __name__ == '__main__':
    unittest.main()
