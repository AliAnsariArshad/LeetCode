from typing import List
from collections import Counter


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while len(nums1) > m:
            nums1.pop(-1)
        nums1 += nums2
        nums1.sort()
        return nums1


s = Solution()
# print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
# print(s.merge(nums1=[1], m=1, nums2=[], n=0))
# print(s.merge(nums1=[0], m=0, nums2=[1], n=1))
print(s.merge(nums1=[1, 0], m=1, nums2=[2], n=1))
