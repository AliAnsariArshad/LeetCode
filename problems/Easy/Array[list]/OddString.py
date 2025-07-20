from typing import List
from collections import Counter

class Solution:
    def oddString(self, words: List[str]) -> str:

        z = []

        for char in words:
            l = []
            i = 0
            j = 1
            while i < len(char) - 1:
                while j < len(char):
                    l.append(ord(char[j]) - ord(char[i]))
                    i += 1
                    j += 1
                z.append(tuple(l))

        d = Counter(z)
        # for item in z:
        #     if item not in d:
        #         d[item] = 1
        #     else:
        #         d[item] = d[item] + 1

        for key in d:
            if d[key] == 1:
                odd = key

        index = z.index(odd)

        return words[index]



s = Solution()
print(s.oddString(words=["adc", "wzy", "abc"]))
print(s.oddString(words=["aaa", "bob", "ccc", "ddd"]))

