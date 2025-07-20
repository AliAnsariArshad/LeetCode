class Solution:
    def longest_nice_sub_string(self, string: str) -> str:
        if len(string) < 2:
            return ""

        unique = set(string)
        for i, c in enumerate(string):
            if c.swapcase() not in unique:
                s1 = self.longest_nice_sub_string(string[0:i])
                s2 = self.longest_nice_sub_string(string[i + 1:])

                return s2 if len(s2) > len(s1) else s1
        return string


s = Solution()
print(s.longest_nice_sub_string("YazaAay"))
print(s.longest_nice_sub_string("Bb"))
print(s.longest_nice_sub_string("c"))
