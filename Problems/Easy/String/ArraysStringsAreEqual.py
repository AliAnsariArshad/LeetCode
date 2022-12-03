from typing import List


class Solution:
    def arrays_strings_are_equal(self, word1: List[str], word2: List[str]) -> bool:
        newword1 = ''.join(word1)
        newword2 = ''.join(word2)

        return newword1 == newword2

    def arrays_strings_are_equal2(self, word1: List[str], word2: List[str]) -> bool:
        newword1 = ''.join(word1)
        newword2 = ''.join(word2)

        if len(newword1) != len(newword2):
            return False

        for i in range(len(newword1)):
            if newword1[i] != newword2[i]:
                return False
        return True


s = Solution()
print(s.arrays_strings_are_equal(word1=["ab", "c"], word2=["a", "bc"]))
print(s.arrays_strings_are_equal(word1=["a", "cb"], word2=["ab", "c"]))
print(s.arrays_strings_are_equal(word1=["abc", "d", "defg"], word2=["abcddefg"]))
print(s.arrays_strings_are_equal2(word1=["ab", "c"], word2=["a", "bc"]))
print(s.arrays_strings_are_equal2(word1=["a", "cb"], word2=["ab", "c"]))
print(s.arrays_strings_are_equal2(word1=["abc", "d", "defg"], word2=["abcddefg"]))