class Solution:
    def find_the_difference(self, s, t):
        x, y = 0, 0
        for i in t:
            x += ord(i)
        for j in s:
            y += ord(j)
        return chr(abs(x - y))


s = Solution()
print(s.find_the_difference("abcd", "abdce"))
