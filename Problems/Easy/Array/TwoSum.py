from typing import List


class Solution:
    """
    1. Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
    target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """

        @param nums: list of integers
        @type nums: integer
        @param target: target number
        @type target: integer
        @return: list of indexes
        @rtype: list of integers
        """
        prev = {}
        for i, v in enumerate(nums):
            remaining = target - nums[i]
            if remaining in prev:
                return [i, prev[remaining]]

            prev[v] = i

    def two_sum_second(self, nums: List[int], target: int) -> List[int]:
        """

        @param nums: list of integers
        @type nums: integer
        @param target: target number
        @type target: integer
        @return: list of indexes
        @rtype: list of integers
        """
        for x in range(0, len(nums)):
            for y in range(0, len(nums)):
                if nums[x] + nums[y] == target:
                    if x != y:
                        return [x, y]
