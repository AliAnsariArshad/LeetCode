class Solution:
    def __init__(self, num):
        self.guess_num = num

    def guess_number(self, n: int) -> int:
        start, end = 1, n

        while end >= start:
            mid = (start + end) // 2
            if self.guess(mid) == 1:
                start = mid + 1
            elif self.guess(mid) == -1:
                end = mid -1
            else:
                return mid
        return -1

    def guess(self, num: int) -> int:

        if self.guess_num < num:
            return -1
        elif self.guess_num > num:
            return 1
        elif num == self.guess_num:
            return 0


s = Solution(4)
print(s.guess_number(5))

s1 = Solution(1)
print(s1.guess_number(1))

s2 = Solution(1)
print(s2.guess_number(2))
