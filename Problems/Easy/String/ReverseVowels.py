class Solution:
    def reverse_vowels(self, s: str) -> str:
        news = ""
        vowels = []
        for char in s:
            if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                vowels.append(char)
        l = len(vowels)
        for char in s:
            if char not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                news += char
            else:
                    news += vowels[l-1]
                    l -= 1
        return news

s = Solution()
print((s.reverse_vowels("hello")))