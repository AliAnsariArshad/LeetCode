from functools import cache


class Solution:
    def climb_stairs(self, num: int) -> int:
        a, b = 0, 1
        for i in range(num):
            a, b = b, a+b
        return b

    def climb_stairs2(self, num: int) -> int:
        @cache
        def fib(num):
            return fib(num-1) + fib(num-2) if num > 1 else num
        return fib(num+1)


s = Solution()
print(s.climb_stairs(num=45))
print(s.climb_stairs2(num=45))
