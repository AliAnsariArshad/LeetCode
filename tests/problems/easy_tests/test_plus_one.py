import unittest
from problems.Easy.AddDigits import Solution


class test_one_plus(unittest.TestCase):

    def test_single_digit_number(self):
        actual = Solution.addDigits(self, 1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_single_digit_boundary_number(self):
        actual = Solution.addDigits(self, 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_double_digit_number(self):
        actual = Solution.addDigits(self, 16)
        expected = 7
        self.assertEqual(actual, expected)

    def test_large_number(self):
        actual = Solution.addDigits(self, 23452341346789)
        expected = 7
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
