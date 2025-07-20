from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = dict(sorted(list(zip(heights, names)), reverse=True))
        return list(n.values())


s= Solution()
print(s.sortPeople(names=["Mary","John","Emma"], heights=[180,165,170]))