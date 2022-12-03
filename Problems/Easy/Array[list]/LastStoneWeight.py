from typing import List


class Solution:
    def last_stone_weight(self, stones: List[int]) -> int:
        num = 0
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 1:
            stones.sort()
            first_max, second_max = stones[-1], stones[-2]
            if first_max == second_max:
                stones.remove(first_max)
                stones.remove(second_max)
            elif first_max != second_max:
                num = first_max - second_max
                stones.remove(first_max)
                stones.remove(second_max)
                stones.append(num)
        return stones[0] if len(stones) == 1 else 0


s = Solution()
print(s.last_stone_weight(stones=[2, 7, 4, 1, 8, 1]))


