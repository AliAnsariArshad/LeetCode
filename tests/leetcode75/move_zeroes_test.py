import unittest

from leetcode75.move_zeros import move_zeroes


class TestArray(unittest.TestCase):

    def test_single_element_zero(self):
        actual = [0]
        expected = [0]

        self.assertEqual(expected, move_zeroes(actual))

    def test_single_element_number(self):
        actual = [1]
        expected = [1]

        self.assertEqual(expected, move_zeroes(actual))

    def test_multiple(self, ):
        actual = [0,1,0,3,12]
        expected = [1,3,12,0,0]

        self.assertEqual(expected, move_zeroes(actual))

    def test_fail(self):
        actual = [0, 1, 0, 3, 12]
        expected = [1, 3, 0, 12, 0]

        self.assertEqual(expected, move_zeroes(actual))