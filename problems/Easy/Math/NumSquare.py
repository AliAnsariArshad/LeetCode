from math import *


class Solution:
    dp = [0]
    def num_squares(self, n: int) -> int:
        """

            @param n:
            @type n:
            @return:
            @rtype:
            """

        if ceil(sqrt(n)) == floor(sqrt(n)):
            return 1

        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        i = 1

        while i * i <= n:
            base = sqrt(n - i * i)
            if base * base == (n - i * i):
                return 2
        return 3

    def num_squares2(self, n: int) -> int:
        dp = self.dp
        per_sqr = [int(pow(i, 2)) for i in range(1, int(sqrt(n))+1)]

        while len(dp) < n+1:
            dpI = inf
            for ps in per_sqr:
                if (len(dp)) < ps:
                    break
                dpI = min(dpI, 1 + dp[-ps])
            dp.append(dpI)

        return dp[n]


s = Solution()
# print(s.num_squares(25))
# print(s.num_squares(9999))
# print(s.num_squares(9998))

print(s.num_squares2(25))
print(s.num_squares2(12))
print(s.num_squares2(9999))
print(s.num_squares2(9998))
