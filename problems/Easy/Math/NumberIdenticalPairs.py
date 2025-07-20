from typing import List


class Solution:
    def num_identical_pairs(self, nums: List[int]) -> int:
        count = 0
        ls = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    # ls.append((i, j))
                    count += 1
        # return len(ls)
        return  count


s = Solution()
print(s.num_identical_pairs(nums=[1, 2, 3, 1, 1, 3]))
print(s.num_identical_pairs(nums=[1, 1, 1, 1]))
print(s.num_identical_pairs(nums=[1, 2, 3]))