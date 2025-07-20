class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            t = s.replace(part, "",1)
            s = t

        return s

    def removeOccurrences2(self, s: str, part: str) -> str:
        while True:
            idx = s.find(part)
            if idx == -1:
                break
            s = s[:idx] + s[idx + len(part):]
        return s


ss = Solution()
# print(ss.removeOccurrences(s="daabcbaabcbc", part="abc"))
print(ss.removeOccurrences(s="aabababa", part="aba"))

print(ss.removeOccurrences2(s="daabcbaabcbc", part="abc"))
print(ss.removeOccurrences2(s="aabababa", part="aba"))