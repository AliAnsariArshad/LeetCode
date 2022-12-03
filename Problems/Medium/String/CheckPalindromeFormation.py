class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        i = 0
        j = len(a) - 1

        ns = b[::-1]

        while i < len(a):
            if a[i] == ns[i]:
                i += 1
                continue
            else:
                break

        newst1 = a[:i] + b[i + 1:]
        newst2 = b[:i] + a[i + 1:]

        if newst1 == newst1[::-1] or newst2 == newst2[::-1]:
            return True
        else:
            return False


ss = Solution()
# print(ss.checkPalindromeFormation(a="ulacfd", b="jizalu"))
# print(ss.checkPalindromeFormation(a="xbdef", b="xecab"))
# print(ss.checkPalindromeFormation(a="x", b="y"))
print(ss.checkPalindromeFormation(a="abdef", b="fecab"))
