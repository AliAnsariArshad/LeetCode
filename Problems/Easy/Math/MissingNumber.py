from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n+1):
            if i not in nums:
                return i

    def missing_number2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        total_sum = len(nums) * (len(nums) + 1) // 2

        for num in nums:
            total_sum -= num

        return total_sum


s = Solution()
print(s.missing_number([3, 0, 1]))
print(s.missing_number([0, 1]))
print(s.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))

print(s.missing_number2([3, 0, 1]))
print(s.missing_number2([0, 1]))
print(s.missing_number2([9, 6, 4, 2, 3, 5, 7, 0, 1]))