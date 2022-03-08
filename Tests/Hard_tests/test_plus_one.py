import unittest
from Problems.Hard.plusOne import Solution


class test_one_plus(unittest.TestCase):

    def test_single_digit_number(self):
        actual = Solution.plus_one(self, [1])
        expected = [2]
        self.assertEqual(actual, expected)

    def test_single_digit_boundary_number(self):
        actual = Solution.plus_one(self, [9])
        expected = [1, 0]
        self.assertEqual(actual, expected)

    def test_double_digit_number(self):
        actual = Solution.plus_one(self, [1, 2])
        expected = [1, 3]
        self.assertEqual(actual, expected)

    def test_double_digit_boundary_number(self):
        actual = Solution.plus_one(self, [9, 9])
        expected = [1, 0, 0]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
