import functools
from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]):
        # ls2 = sorted(strs, key=len)
        # print(ls2)
        if len(strs) == 0:
            return ""
        shortest = min(strs, key=len)
        strs.remove(shortest)
        prefix = ""
        for j in range(len(shortest)):
            for st in strs:
                if shortest[j] == st[j]:
                    if prefix == "" or (shortest[j] not in prefix):
                        prefix = prefix + shortest[j]
                else:

                    return prefix

        return prefix

    def longest_common_prefix_2(self, strs: List[str]):

        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i = i + 1
            else:
                break
        return str1[:i]

    # @return a string
    def longest_commonprefix(self, strs):
        if not strs:
            return ''
        else:
            return functools.reduce(self.lcp, strs)


s = Solution()
# print(s.longest_common_prefix([]))
print(s.longest_commonprefix(["flower", "flow", "flight", "fl"]))
print(s.longest_common_prefix_2(["dog","racecar","car"]))
