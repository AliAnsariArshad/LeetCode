import unittest
from Problems.Easy.Array.RemoveDupliates import Solution


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicate_1(self):
        actual = Solution.remove_duplicates(self, nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
        expected = 5
        self.assertEqual(actual, expected)

    def test_remove_duplicate_2(self):
        actual = Solution.remove_duplicates(self, nums=[1, 1, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_remove_duplicate_2_1(self):
        actual = Solution.remove_duplicates_2(self, nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
        expected = 5
        self.assertEqual(actual, expected)

    def test_remove_duplicate_2_2(self):
        actual = Solution.remove_duplicates_2(self, nums=[1, 1, 2])
        expected = 2
        self.assertEqual(actual, expected)
