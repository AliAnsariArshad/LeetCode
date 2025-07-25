from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] == 0:
                    continue
                else:
                    a = nums[i]
                    nums[i] = nums[j]
                    nums[j] = a
    return nums