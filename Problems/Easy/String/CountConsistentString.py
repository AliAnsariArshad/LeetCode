from typing import List


class Solution:
    def count_consistent_strings(self, allowed: str, words: List[str]) -> int:
        count = 0
        flag = True
        for item in words:
            for i in range(len(item)):
                if item[i] in allowed:
                    flag = True
                    continue
                else:
                    flag = False
                    break
            if flag:
                count += 1

        return count

    def count_consistent_strings2(self, allowed: str, words: List[str]) -> int:
        count = 0
        for item in words:
            for char in item:
                if char not in allowed:
                    count += 1
                    break
        return len(words) - count


s = Solution()
print(s.count_consistent_strings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))
print(s.count_consistent_strings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(s.count_consistent_strings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
print(s.count_consistent_strings2(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))
print(s.count_consistent_strings2(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(s.count_consistent_strings2(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
