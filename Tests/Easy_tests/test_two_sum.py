import unittest
from Problems.Easy.Array.TwoSum import Solution


class TestTwoSum(unittest.TestCase):

    def test_two_sum_1(self):
        actual = Solution.two_sum(self, nums=[2, 7, 11, 15], target=9)
        expected = [0, 1]
        actual.sort()
        expected.sort()
        self.assertEqual(actual, expected)

    def test_two_sum_2(self):
        actual = Solution.two_sum(self, nums=[3, 2, 3], target=6)
        expected = [0, 2]
        actual.sort()
        expected.sort()
        self.assertEqual(actual, expected)

    def test_two_sum_3(self):
        actual = Solution.two_sum(self, nums=[3, 3], target=6)
        expected = [0, 1]
        actual.sort()
        expected.sort()
        self.assertEqual(actual, expected)

    def test_two_sum_second_1(self):
        actual = Solution.two_sum_second(self, nums=[2, 7, 11, 15], target=9)
        expected = [0, 1]
        actual.sort()
        expected.sort()
        self.assertEqual(actual, expected)

    def test_two_sum_second_2(self):
        actual = Solution.two_sum_second(self, nums=[3, 2, 3], target=6)
        expected = [0, 2]
        actual.sort()
        expected.sort()
        self.assertEqual(actual, expected)

    def test_two_sum_second_3(self):
        actual = Solution.two_sum_second(self, nums=[3, 3], target=6)
        expected = [0, 1]
        actual.sort()
        expected.sort()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
