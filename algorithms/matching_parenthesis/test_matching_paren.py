import unittest
from matching_paren import matching_paren

class TestMatchingParen(unittest.TestCase):
    def test_matching_paren(self):
        self.assertEqual(matching_paren('(({[]}))'), True)
        self.assertEqual(matching_paren('()[]{}'), True)
        self.assertEqual(matching_paren('(()))[['), False)
        self.assertEqual(matching_paren('(())[[]]'), True)
        self.assertEqual(matching_paren('{(({{[]}})()[])}'),  True)
        self.assertEqual(matching_paren('(()))[[]]{}((([[{{(})}}]])))'), False)

if __name__ == '__main__':
    unittest.main()
