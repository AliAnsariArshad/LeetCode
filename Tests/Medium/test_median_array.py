import unittest
from Problems.Medium.medianTwoSortedArrays import Solution


class test_median_two_sorted_arrays(unittest.TestCase):

    def test_first(self):
        actual = Solution.findMedianSortedArrays(self, [1, 3], [2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_second(self):
        actual = Solution.findMedianSortedArrays(self, [1, 2], [3, 4])
        expected = 2.5
        self.assertEqual(actual, expected)

    def test_third(self):
        actual = Solution.findMedianSortedArrays(self, [1, 4, 5], [2, 3, 6])
        expected = 3.5
        self.assertEqual(actual, expected)

    def test_forth(self):
        actual = Solution.findMedianSortedArrays(self, [1, 4, 5], [2, 3, 6, 7])
        expected = 4
        self.assertEqual(actual, expected)

    def test_fifth(self):
        actual = Solution.findMedianSortedArrays(self, [0], [0])
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_method(self):
        actual = Solution.findMedianSortedArrays2(self, [1, 3], [2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_second_method(self):
        actual = Solution.findMedianSortedArrays2(self, [1, 2], [3, 4])
        expected = 2.5
        self.assertEqual(actual, expected)

    def test_third_method(self):
        actual = Solution.findMedianSortedArrays2(self, [1, 4, 5], [2, 3, 6])
        expected = 3.5
        self.assertEqual(actual, expected)

    def test_forth_method(self):
        actual = Solution.findMedianSortedArrays2(self, [1, 4, 5], [2, 3, 6, 7])
        expected = 4
        self.assertEqual(actual, expected)

    def test_fifth_method(self):
        actual = Solution.findMedianSortedArrays2(self, [0], [0])
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
