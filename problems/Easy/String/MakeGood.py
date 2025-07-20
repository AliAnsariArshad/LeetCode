class Solution:

    def make_good(self, s: str) -> str:
        if len(s) < 2:
            return s

        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                isUp = stack[-1].isupper()
                isLow = s[i].islower()

                if isUp == isLow and stack[-1].lower() == s[i].lower():
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        return "".join(stack)



sr = Solution()
print(sr.make_good("leEeetcode"))