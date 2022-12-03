from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = [x for x in nums if x % 2 == 0 and x % 3 == 0]

        return 0 if len(s) == 0 else sum(s)//len(s)

    def averageValue2(self, nums: List[int]) -> int:
        nums = [x for x in nums if x % 6 == 0]
        return sum(nums)//len(nums) if nums else 0


s = Solution()
print(s.averageValue(nums=[1, 3, 6, 10, 12, 15]))
print(s.averageValue2(nums=[1, 3, 6, 10, 12, 15]))
