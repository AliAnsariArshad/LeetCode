from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        d = {}
        for rs in list1:
            if rs in list2:
                d[rs] = list1.index(rs) + list2.index(rs)

        sum = min(d.values())
        for keys in d:
            if d[keys] == sum:
                result.append(keys)

        return result

ss = Solution()
print(ss.findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))
