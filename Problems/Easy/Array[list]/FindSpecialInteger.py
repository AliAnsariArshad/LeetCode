from collections import Counter
from typing import List


class Solution:
    def find_special_integer(self, arr: List[int]) -> int:
        counter = Counter(arr)
        d = {}
        for key in counter:
            if (counter[key] / len(arr)) * 100 >= 25:
                d[key] = (counter[key] / len(arr)) * 100

        s = max(d.values())
        for key in d:
            if d[key] == s:
                return key

    def find_special_integer2(self, arr: List[int]) -> int:
        # s= [(i,x) for i, x in arr x if arr.count(i) / 4 >= 25 ]
        num = 0
        per = 0
        cur = 0
        for i in arr:
            per = arr.count(i) / len(arr) * 100
            if per > cur:
                cur = per
                num = i

        return num



s = Solution()
print(s.find_special_integer(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(s.find_special_integer2(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(s.find_special_integer2(arr=[1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]))
