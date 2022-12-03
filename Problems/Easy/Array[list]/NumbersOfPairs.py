from collections import Counter
from typing import List


class Solution:
    def number_of_pairs(self, nums: List[int]) -> List[int]:
        pair_count = 0
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                pair_count += 1
                result.remove(i)

        return [pair_count, len(result)]

    def number_of_pairs2(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        pairs_count = 0
        left_overs = 0
        for _, values in counter.items():
            pairs_count += values // 2
            left_overs += values % 2
        return [pairs_count, left_overs]


s = Solution()
print(s.number_of_pairs(nums=[1, 3, 2, 1, 3, 2, 2]))
print(s.number_of_pairs2(nums=[1, 3, 2, 1, 3, 2, 2]))
