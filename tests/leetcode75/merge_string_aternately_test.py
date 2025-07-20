import unittest
from array import array

from leet_code_75.merge_strings_alternately import Solution


class TestArray(unittest.TestCase):
    solution = Solution()

    def test_same_length(self):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"

        self.assertEqual(expected, self.solution.merge_alternately(word1, word2))

    def test_first_string_greater(self):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"

        self.assertEqual(expected, self.solution.merge_alternately(word1, word2))

    def test_second_string_greater(self):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"

        self.assertEqual(expected, self.solution.merge_alternately(word1, word2))

    def test_same_length_1(self):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"

        self.assertEqual(expected, self.solution.merge_alternately_single_pointer(word1, word2))

    def test_first_string_greater_1(self):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"

        self.assertEqual(expected, self.solution.merge_alternately_single_pointer(word1, word2))

    def test_second_string_greater_1(self):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"

        self.assertEqual(expected, self.solution.merge_alternately_single_pointer(word1, word2))

    def test_same_length_2(self):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"

        self.assertEqual(expected, self.solution.merge_alternately_double_pointer(word1, word2))

    def test_first_string_greater_2(self):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"

        self.assertEqual(expected, self.solution.merge_alternately_double_pointer(word1, word2))

    def test_second_string_greater_2(self):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"

        self.assertEqual(expected, self.solution.merge_alternately_double_pointer(word1, word2))

