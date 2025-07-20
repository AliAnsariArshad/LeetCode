class Solution:

    def __init__(self, num):
        self.bad_version = num

    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        if n == 1 and self.isBadVersion(n):
            return 1
        while start <= end:
            mid = (start + end) // 2
            if self.isBadVersion(mid):
                if not self.isBadVersion(mid-1):
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid+1

        return 0

    def isBadVersion(self, n: int) -> bool:

        if n >= self.bad_version:
            return True
        else:
            return False


s = Solution(4)
print(s.firstBadVersion(5))
