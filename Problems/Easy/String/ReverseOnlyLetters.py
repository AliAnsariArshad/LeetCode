class Solution:
    def reverse_only_letter(self, s: str):
        result = []

        for i in range(len(s)):
            if s[i].isalpha():
                result.append(s[i])
        result1 = result[::-1]

        for char in range(len(s)):
            if s[char].isalpha():
                continue
            else:
                result1.insert(char, s[char])
        return ''.join(result1)

    def reverse_only_letters(self, s: str):
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif not s[l].isalpha():
                l += 1
            elif not s[r].isalpha():
                r -= 1
        return "".join(s)

    def reverse_only_letter2(self, s: str):
        english, non_english = [], []
        for i,c in enumerate(s):
            if c.isalpha():
                english.append(c)
            else:
                non_english.append((i,c))
        english = english[::-1]
        for ind, sep in non_english:
            english.insert(ind,sep)
        return "".join(english)


s = Solution()
print(s.reverse_only_letter("Test1ng-Leet=code-Q!"))
print(s.reverse_only_letters("Test1ng-Leet=code-Q!"))
print(s.reverse_only_letter2("Test1ng-Leet=code-Q!"))
