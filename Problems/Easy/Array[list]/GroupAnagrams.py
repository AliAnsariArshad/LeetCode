from collections import Counter
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for items in strs:
            sortedString = "".join(sorted(items))

            if sortedString in anagrams:
                anagrams[sortedString].append(items)
            else:
                anagrams[sortedString] = [items]

        return list(anagrams.values())


s = Solution()
print(s.group_anagrams(strs = ["eat","tea","tan","ate","nat","bat"]))