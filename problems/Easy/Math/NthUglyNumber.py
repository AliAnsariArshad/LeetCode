class Solution:
    def nth_ugly_number(self, n: int) -> int:
        arr = [1]

        for i in range(2, n+1):
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                arr.append(i)

        return arr[n]


s = Solution()
print(s.nth_ugly_number(n=10))
