class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        hl = int(len(s) / 2)
        fh = s[:hl]
        sh = s[hl:]
        vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        count1 = 0
        count2 = 0
        for i in fh:
            if i in vowel:
                count1 += 1

        for i in sh:
            if i in vowel:
                count2 += 1

        return count1 == count2


ss = Solution()
print(ss.halvesAreAlike(s='book'))
print(ss.halvesAreAlike(s='textbook'))