from typing import List


class Solution:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        stair1 = cost[0]
        stair2 = cost[1]
        cost.append(0)
        for i in range(2, len(cost)):
            c = min(stair1, stair2) + cost[i]
            stair1 = stair2
            stair2 = c
        return c


s = Solution()
print(s.min_cost_climbing_stairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(s.min_cost_climbing_stairs(cost=[10, 15, 20]))


