from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        s = [num for num in nums if num %2 == 0]
        d = {}
        for num in s:
            if num not in d.values():
                d[s.count(num)] = num

        return d



s = Solution()
print(s.mostFrequentEven(nums=[0, 1, 2, 2, 4, 4, 1]))
