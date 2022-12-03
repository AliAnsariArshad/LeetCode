from typing import List


class Solution:
    def find_gcd(self, nums: List[int]) -> int:
        nums.sort()
        lis = []
        a = nums[0]
        b = nums[-1]
        d = min(a, b)
        for i in range(1, d+1):
            if a % i == 0 and b % i == 0:
                lis.append(i)
        return 1 if len(lis) == 0 else max(lis)

    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        result = 1
        for i in range(2, min_num + 1):
            if min_num % i == 0 and max_num % i == 0:
                result = i
        return result


s = Solution()
print(s.findGCD([2,5,6,9,10]))


