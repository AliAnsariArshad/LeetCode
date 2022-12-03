import unittest
from Problems.Easy.Math.Tribonacci import Solution


class TestTribonacci(unittest.TestCase):

    def test_tribonacci(self):
        actual = Solution.tribonacci(self, num=25)
        expected = 1389537
        self.assertEqual(actual, expected)

    def test_tribonacci_2(self):
        actual = Solution.tribonacci2(self, num=25)
        expected = 1389537
        self.assertEqual(actual, expected)

    def test_tribonacci_3(self):
        actual = Solution.tribonacci3(self, num=25)
        expected = 1389537
        self.assertEqual(actual, expected)

    if __name__ == '__main__':
     unittest.main()