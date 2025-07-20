from collections import Counter


class Solution:
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False
        s_counter, t_counter = Counter(s), Counter(t)
        for char in s_counter:
            if s_counter[char] != t_counter[char]:
                return False
        return True

    def is_anagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = {}

        for char in s:
            if char not in s_chars.keys():
                s_chars[char] = 1
            else:
                s_chars[char] += 1

        for char in t:
            if char in s_chars.keys() and s_chars[char] > 0:
                s_chars[char] -= 1
            else:
                return False

        return True




s = Solution()
print(s.is_anagram2("anagram", "nagaram"))
print(s.is_anagram2("rat", "car"))