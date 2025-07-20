import math
from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        d = Counter(tasks).values()

        return -1 if 1 in d else sum((a+2)//3 for a in d)

    def minimumRounds2(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        res = 0
        for i, n in c.items():
            if n < 2:
                return -1
            res += math.ceil(n / 3)
        return res

    def minimumRounds3(self, tasks: List[int]) -> int:
        rounds, counts = 0, Counter(tasks)
        for item in counts:
            if counts[item] == 1:
                return -1
            rounds += int(math.ceil(counts[item] / 3))
        return rounds


s = Solution()
print(s.minimumRounds(tasks = [2,2,3,3,2,4,4,4,4,4]))
print(s.minimumRounds(tasks = [2, 3, 3]))
print(s.minimumRounds(tasks = [2, 2, 2, 2]))

print(s.minimumRounds2(tasks = [2,2,3,3,2,4,4,4,4,4]))
print(s.minimumRounds2(tasks = [2, 3, 3]))
print(s.minimumRounds2(tasks = [2, 2, 2, 2]))