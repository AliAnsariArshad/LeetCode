import math


class Solution:
    def common_factor(self, a: int, b: int) -> int:
        arange = a//2
        brange = b//2
        alist = []
        blist = []
        result = 0
        for i in range(1, arange+1):
            if a % i == 0:
                alist.append(i)
        alist.append(a)
        for j in range(1, brange+1):
            if b % j == 0:
                blist.append(j)
        blist.append(b)
        for char in alist:
            if char in blist:
                result += 1

        return result

    def common_factor2(self, a: int, b: int) -> int:
        arange = a//2
        brange = b//2
        drange = arange if arange > brange else brange
        alist = []
        blist = []
        result = 0
        for i in range(1, drange+1):
            if a % i == 0:
                alist.append(i)
            if b % i == 0:
                blist.append(i)
        alist.append(a)
        blist.append(b)
        for char in alist:
            if char in blist:
                result += 1

        return result

    def common_factor3(self, a: int, b: int) -> int:
        greates_common_divisor = math.gcd(a, b)

        count = 1
        for i in range(2, greates_common_divisor+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count

    def common_factors4(self, a: int, b: int) -> int:
        result = 1
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                result += 1
        return result



s = Solution()
print(s.common_factors4(12, 6))
