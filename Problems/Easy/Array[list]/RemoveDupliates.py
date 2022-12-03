from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                if i != j:
                    nums[i] = nums[j]
                i += 1
        return i

    def remove_duplicates2(self, nums: List[int]) -> int:
        i = 1

        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i+= 1
        return i





s = Solution()
print(s.remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.remove_duplicates([1,1,2]))
print(s.remove_duplicates2([0,0,1,1,1,2,2,3,3,4]))
print(s.remove_duplicates2([1,1,2]))