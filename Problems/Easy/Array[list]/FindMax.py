from typing import List


class Solution:
    def find_max(self, nums: List[int]) -> int:
        nums.sort()
        n = []
        for num in nums:
            if abs(num) == (-1)* num:
                n.append(num)

        for num in n:
            if abs(num) in nums:
                return abs(num)
            continue
        return -1

    def find_max2(self, nums: List[int]) -> int:
        nums = set(nums)
        ret = -1
        for i in nums:
            if -i in nums:
                ret = max(ret, i)
        return ret


s = Solution()
print(s.find_max(nums=[-1, 10, 6, 7, -7, 1]))
print(s.find_max(nums=[14,33,40,-33,8,-24,-42,30,-18,-34]))
print(s.find_max2(nums=[14,33,40,-33,8,-24,-42,30,-18,-34]))