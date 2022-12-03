from collections import Counter
from typing import List


class Solution:
    def common_chars(self, words: List[str]) -> List[str]:
        sortedlist = [word for word in sorted(words, key=len)]
        count = Counter(sortedlist[0])
        for item in sortedlist:
            count &= Counter(item)
        return list(count.elements())

    def common_chars2(self, words: List[str]) -> List[str]:
        if len(words) < 2:
           return list(words[0])

        common_chas = []
        seen = set(words[0])
        for char in seen:
            count = min([word.count(char) for word in words])

            if count > 0:
                common_chas.extend(char*count)

        return common_chas

s = Solution()
print(s.common_chars(words=["bella", "label", "roller"]))
print(s.common_chars(words=["cool","lock","cook"]))

print(s.common_chars2(words=["bella", "label", "roller"]))
print(s.common_chars2(words=["cool","lock","cook"]))


