import collections
from typing import List


class Solution:
    """
    2475. Number of Unequal Triplets in Array
    """

    def unequal_triplets(self, nums: List[int]):
        count = 0
        arr = []

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1
                        arr.append([i, j, k])

        return count, arr

    def unequal_triplets2(self, nums: List[int]):
        trips = pairs = 0
        count = collections.defaultdict(int)
        for i, a in enumerate(nums):
            trips += pairs - count[a] * (i - count[a])
            pairs += i - count[a]
            count[a] += 1
        return trips


s = Solution()
print(s.unequal_triplets2(nums=[4, 4, 2, 4, 3]))
