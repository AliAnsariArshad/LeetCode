import collections
from typing import List


class Solution:
    """
    18. 4Sum
    """

    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        """

        @param nums:
        @type nums:
        @param target:
        @type target:
        @return:
        @rtype:
        """
        arr = []

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for z in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[z] == target:
                            arrr = []
                            arrr.append(nums[i])
                            arrr.append(nums[j])
                            arrr.append(nums[k])
                            arrr.append(nums[z])
                            # arrr.sort()
                            if arrr not in arr:
                                arr.append(arrr)

        d = {}
        for item in arr:
            item.sort()
            if tuple(item) not in d:

                d[tuple(item)] = 1
            else:
                d[tuple(item)] += 1
        # return d

        for item in arr:
            item.sort()
            while d[tuple(item)] > 1:
                a = item
                arr.remove(a)
                d[tuple(item)] -= 1
        return arr


s = Solution()
# print(s.four_sum(nums=[1, 0, -1, 0, -2, 2], target=0))
# print(s.four_sum(nums=[-5, 5, 4, -3, 0, 0, 4, -2], target=4))
print(s.four_sum(nums=[5, 5, 3, 5, 1, -5, 1, -2], target=4))
