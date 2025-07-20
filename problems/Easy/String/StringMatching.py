import copy
from typing import List


class Solution:
    def string_matching(self, words: List[str])-> List[str]:
        ls = []
        result = []
        for item in words:
            ls = copy.copy(words)
            ls.remove(item)
            for char in ls:
                if char in item:
                    if char not in result:
                        result.append(char)
        return result


s = Solution()
print(s.string_matching(words=["mass", "as", "hero", "superhero"]))
print(s.string_matching(words=["leetcode", "et", "code"]))
print(s.string_matching(words=[]))
