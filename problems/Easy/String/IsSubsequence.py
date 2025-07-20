class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t) :
            return False
        if len(s) == 0:
            return True
        sub = 0
        news = ""
        slen = len(s) -1
        for i in range(len(t)):
            if sub <= slen:
                if s[sub] == t[i]:
                    sub += 1
                    news += ''.join((t[i]))

        return news == s


    def is_subsequence2(self, s: str, t: str) -> bool:
        '''
        Using pointer
        '''
        sl = tl = 0
        while sl < len(s) and tl < len(t):
            if s[sl] == t[tl]:
                sl += 1
            tl += 1

        return sl == len(s)

    def is_subsequence3(self, s: str, t: str) -> bool:
        '''
        Using pointer
        '''
        if not s:
            return True

        i = 0

        for char in t:
            if char == s[i]:
                i += 1
            if i == len(s):
                break

        return i == len(s)

s = Solution()
print(s.is_subsequence(s='abc', t='ahbgdc'))
print(s.is_subsequence(s='axc', t='ahbgdc'))
print(s.is_subsequence(s='acb', t='ahbgdc'))
print(s.is_subsequence2(s='abc', t='ahbgdc'))
print(s.is_subsequence2(s='axc', t='ahbgdc'))
print(s.is_subsequence2(s='acb', t='ahbgdc'))
# print(s.is_subsequence3(s='abc', t='ahbgdc'))
# print(s.is_subsequence3(s='axc', t='ahbgdc'))
print(s.is_subsequence3(s='acb', t='ahbgdc'))