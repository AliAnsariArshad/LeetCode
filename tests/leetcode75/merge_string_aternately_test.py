import unittest

from leetcode75.merge_strings_alternately import (merge_alternately_double_pointer, merge_alternately,
                                                  merge_alternately_single_pointer)


class TestArray(unittest.TestCase):

    def test_same_length(self):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"

        self.assertEqual(expected, merge_alternately(word1, word2))

    def test_first_string_greater(self):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"

        self.assertEqual(expected, merge_alternately(word1, word2))

    def test_second_string_greater(self):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"

        self.assertEqual(expected, merge_alternately(word1, word2))

    def test_same_length_1(self):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"

        self.assertEqual(expected, merge_alternately_single_pointer(word1, word2))

    def test_first_string_greater_1(self):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"

        self.assertEqual(expected, merge_alternately_single_pointer(word1, word2))

    def test_second_string_greater_1(self):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"

        self.assertEqual(expected, merge_alternately_single_pointer(word1, word2))

    def test_same_length_2(self):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"

        self.assertEqual(expected, merge_alternately_double_pointer(word1, word2))

    def test_first_string_greater_2(self):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"

        self.assertEqual(expected, merge_alternately_double_pointer(word1, word2))

    def test_second_string_greater_2(self):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"

        self.assertEqual(expected, merge_alternately_double_pointer(word1, word2))
