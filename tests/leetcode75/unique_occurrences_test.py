import unittest

from leetcode75.unique_occurrences_1207 import (unique_occurrences,
                                                unique_occurrences_2,
                                                unique_occurrences_3)

class TestArray(unittest.TestCase):

    def test_true_1(self):
        arr = [1,2,2,1,1,3]
        expected = True

        self.assertEqual(expected, unique_occurrences(arr))

    def test_false_1(self):
        arr = [1,2]
        expected = False
        self.assertEqual(expected, unique_occurrences(arr))

    def test_true_13(self):
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
        expected = True

        self.assertEqual(expected, unique_occurrences(arr))


    def test_true_2(self):
        arr = [1,2,2,1,1,3]
        expected = True

        self.assertEqual(expected, unique_occurrences_2(arr))

    def test_false_2(self):
        arr = [1,2]
        expected = False
        self.assertEqual(expected, unique_occurrences_2(arr))

    def test_true_23(self):
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
        expected = True

        self.assertEqual(expected, unique_occurrences_2(arr))

    def test_true_3(self):
        arr = [1,2,2,1,1,3]
        expected = True

        self.assertEqual(expected, unique_occurrences_3(arr))

    def test_false_3(self):
        arr = [1,2]
        expected = False
        self.assertEqual(expected, unique_occurrences_3(arr))

    def test_true_33(self):
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
        expected = True

        self.assertEqual(expected, unique_occurrences_3(arr))
