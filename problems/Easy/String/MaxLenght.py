from typing import List


class Solution:
    def max_length(self, arr: List[str]) -> int:
        ls = []
        for item in arr:
            unique = set(item)
            if len(unique) == len(item):
                ls.append(unique)
        substrings = [set()]
        for i in ls:
            for j in substrings:
                if not j & i:
                    substrings.append(j | i)
        return max(len(substring) for substring in substrings)



s = Solution()
# print(s.max_length(["abcdefghijklmnopqrstuvwxyz"]))
# print(s.max_length(["cha","r","act","ers"]))
print(s.max_length(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))
print(s.max_length(["a"]))