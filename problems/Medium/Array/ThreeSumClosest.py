from typing import List
from math import *


class Solution:
    """
    16. 3Sum Closest
    """

    def three_sum_closest(self, nums: List[int], target: int) -> int:
        """

        @param nums:
        @type nums:
        @param target:
        @type target:
        @return:
        @rtype:
        """

        diff = inf
        total = result = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if abs(diff) > abs(total - target):
                        diff = total - target
                        result = total
        return result

    def three_sum_closest2(self, nums: List[int], target: int) -> int:
        """
        Two pointer approach
        @param nums:
        @type nums:
        @param target:
        @type target:
        @return:
        @rtype:
        """
        nums.sort()
        diff = inf
        total = result = 0
        i = 0
        length = len(nums)

        while i < length - 2:
            j, k = i + 1, length - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(diff) > abs(total - target):
                    diff = total - target
                    result = total
                if total < target:
                    j += 1
                else:
                    k -= 1
            i += 1

        return result


s = Solution()
print(s.three_sum_closest(nums=[-1, 2, 1, -4], target=1))
print(s.three_sum_closest2(nums=[-1, 2, 1, -4], target=1))
