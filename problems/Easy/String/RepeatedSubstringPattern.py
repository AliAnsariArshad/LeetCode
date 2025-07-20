class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
       news = "".join((s[1:], s[:-1]))
       return s in news


ss = Solution()
print(ss.repeatedSubstringPattern("ababba"))
print(ss.repeatedSubstringPattern("abcabcabcabc"))
