from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                curr_num = num
                curr_len = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len


ss = Solution()
# print(ss.longest_consecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(ss.longest_consecutive(nums=[100, 4, 200, 1, 3, 2]))
print(ss.longest_consecutive(nums=[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))

