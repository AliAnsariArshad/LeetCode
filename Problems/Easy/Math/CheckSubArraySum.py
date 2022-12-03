from typing import List


class Solution:
    def check_sub_array_sum(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False

        seen = {0:-1}
        mod = 0

        for i, num in enumerate(nums):
            mod = (num + mod) % k

            if mod == 0 and num != 0 and i > 0:
                return True
            elif mod in seen:
                if i - seen[mod] >= 2:
                    return True
            else:
                seen[mod] = i

        return False

    def check_sub_array_sum2(self, nums: List[int], k: int) -> bool:
        mod = 0
        seen = {0: -1}
        for i, n in enumerate(nums):
            mod += n
            r = mod % k
            if r not in seen:
                seen[r] = i
            elif i - seen[r] > 1:
                return True
        return False


s = Solution()
print(s.check_sub_array_sum2(nums=[23, 2, 6, 4, 7], k=6))
