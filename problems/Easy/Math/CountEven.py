class Solution:
    def count_even(self, num: int) -> int:
        n, dSum = num, 0
        while n > 0:  # Calculate digit sum of numbers
            dSum += n % 10
            n = n // 10
        if num % 2 == 0 and dSum % 2 == 1:
            return num // 2 - 1
        return num // 2

    def count_even2(self, num: int) -> int:
        if num % 2:
            return num // 2
        return num // 2 - sum(map(int, str(num))) % 2


s = Solution()
print(s.count_even2(91))

