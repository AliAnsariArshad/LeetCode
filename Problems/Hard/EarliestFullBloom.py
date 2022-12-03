from typing import List


class Solution:
    def earliest_full_bloom(self, plant_time: List[int], grow_time: List[int]) -> int:

        acc_plant = 0
        min_time = 0
        s = reversed(sorted(zip(grow_time, plant_time)))

        for grow, cur_plant in s:
            log_str = " " * acc_plant + "."* cur_plant + "^" * grow
            print(log_str)
            acc_plant += cur_plant
            min_time = max(min_time, len(log_str))

        return min_time

    def earliest_full_bloom2(self, plant_time: List[int], grow_time: List[int]) -> int:
        res = 0
        for grow, plant in sorted(zip(grow_time, plant_time)):
            res = max(res, grow) + plant
        return res


s = Solution()
print(s.earliest_full_bloom(plant_time=[1, 2, 3, 2], grow_time=[2, 1, 2, 1]))
print()
print("=============================================")
print()
print(s.earliest_full_bloom(plant_time=[1, 4, 3], grow_time=[2, 3, 1]))

print(s.earliest_full_bloom2(plant_time=[1, 2, 3, 2], grow_time=[2, 1, 2, 1]))

