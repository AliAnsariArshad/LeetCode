from functools import cache


class Solution:
    def tribonacci(self, num: int) -> int:
        if num in (0, 1):
            return num
        if num == 2:
            return 1
        a = 0
        b = 1
        c = 1
        i = 3
        temp = 0
        while i <= num:
            temp = a + b + c
            a = b
            b = c
            c = temp
            i += 1

        return temp

    @cache
    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        else:
            return Solution.tribonacci2(self, n - 1) + Solution.tribonacci2(self, n - 2) + Solution.tribonacci2(self,
                                                                                                             n - 3)
    
    def tribonacci3(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        temp = 0
        if n in [1, 0]:
            return n
        elif n == 2:
            return 1
        else:
            for i in range(3, n+1):
                temp = a + b + c
                a, b, c = b, c, temp
        return temp
                
            

s = Solution()
print(s.tribonacci(num=25))
print(s.tribonacci2(n=25))
print(s.tribonacci3(n=25))
