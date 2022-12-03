from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i, j, k = 0,0,0

        while i < len(nums)-2:
            j = i + 1
            if not nums[i]< nums[j]:
                j += 1
                continue
            k = j + 1
            if not nums[k] < nums[j]:
                k += 1
                continue
            if nums[i] < nums[k] < nums[j]:
                        return True
            i += 1
        return False

    def find132pattern2(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] < nums[j]:
                    for k in range(j + 1, len(nums)):
                        if nums[k] < nums[j]:
                            if nums[i] < nums[k] < nums[j]:
                                return True
                            else:
                                break
                        else:
                            break
                else:
                    break
        return False


s = Solution()
# print(s.find132pattern([3,1,4,2]))
print(s.find132pattern([3,5,0,3,4]))

print(s.find132pattern2([3,1,4,2]))
print(s.find132pattern2([3,5,0,3,4]))