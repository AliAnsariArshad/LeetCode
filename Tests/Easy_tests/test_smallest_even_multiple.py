import unittest
from Problems.Easy.Math.SmallestEvenMultiple import Solution


class TestSmallestEvenMultiple(unittest.TestCase):

    def test_smallest_even_multiple(self):
        actual = Solution.smallest_even_multiple(self, n=9)
        expected = 18
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()


