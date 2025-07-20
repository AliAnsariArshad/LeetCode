from typing import List


class Solution:
    def count_bits(self, num: int) -> List[int]:
        return [int(str(bin(i)).replace("0b", '').count('1')) for i in range(num+1)]

    def count_bits2(self, num: int) -> List[int]:
        return [int(str(bin(i))[2:].count('1')) for i in range(num+1)]



s = Solution()
print(s.count_bits(5))
