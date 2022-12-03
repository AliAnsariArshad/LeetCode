from collections import Counter
from typing import List


class Solution:
    def find_error_nums(self, nums: List[int]):
        count = Counter(nums)
        result = []
        newlist = []
        for i in range(1, len(nums) + 1):
            newlist.append(i)
        for i in newlist:
            if i in nums:
                continue
            else:
                for key in count:
                    if count[key] == 2:
                        result.append(key)
                result.append(i)
        return result

    def find_error_nums2(self, nums: List[int]):
        result  = []
        new_list = [i for i in range(1, len(nums)+1)]
        nums.sort()

        for i in new_list:
            if i not in nums:
                result.insert(0, i)
            if nums.count(i) == 2:
                result.insert(-1,i)


        return result

    def find_error_nums3(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = [0,0]
        for i in range(1, len(nums)+1):
            if count[i] == 2:
                result[0] = i
            if count[i] == 0:
                result[1] = i
        return result

    def find_error_nums4(self, nums: List[int]) -> List[int]:
        n, a, b = len(nums), sum(nums), sum(set(nums))

        s = n * (n + 1) // 2

        return [a - b, s - b]


s = Solution()
print(s.find_error_nums2([2,2]))