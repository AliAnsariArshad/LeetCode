from collections import defaultdict
from typing import List


class Solution:
    def merge_similar_items(self, items1: List[List[int]], items2: List[List[int]]):
        result = []
        merged_items = items1 + items2

        d = defaultdict(int)

        for item in merged_items:
            value, weight = item
            d[value] = d[value] + weight

        for item in sorted(d):
            result.append([item, d[item]])

        return result

    def merge_similar_items2(self, items1: List[List[int]], items2: List[List[int]]):
        d = dict(items1)
        for [i, v] in items2:
            d[i] = d.get(i, 0) + v
        ans = list(d.items())
        ans.sort(key=lambda a: a[0])
        return ans

    def merge_similar_items3(self, items1: List[List[int]], items2: List[List[int]]):
        d = {}
        for i in range(len(items1)):
            if items1[i][0] in d:
                d[items1[i][0]] += items1[i][1]
            else:
                d[items1[i][0]] = items1[i][1]
        for i in range(len(items2)):
            if items2[i][0] in d:
                d[items2[i][0]] += items2[i][1]
            else:
                d[items2[i][0]] = items2[i][1]
        return sorted(d.items())


s = Solution()
print(s.merge_similar_items(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
print(s.merge_similar_items2(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
print(s.merge_similar_items3(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
