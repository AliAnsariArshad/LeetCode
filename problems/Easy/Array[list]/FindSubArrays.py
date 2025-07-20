from typing import List
from collections import defaultdict


class Solution:
    def find_sub_arrays(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return False
        d = defaultdict(List[int])
        sum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum not in d:
                    d[sum] = [nums[i], nums[j]]
                else:
                    d[sum] = d[sum] + [nums[i], nums[j]]
        for key, values in d.items():
            if d[key] == 2:
                return True
            else:
                return False

s = Solution()
print(s.find_sub_arrays(nums = [4,2,4]))