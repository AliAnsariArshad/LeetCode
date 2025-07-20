from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        result = []
        y_axis = []
        z = min([min(x) for x in trees])
        p0 = [item for item in trees if item[1]==z][0]
        # trees.sort(key=lambda p: )
        # for item in trees:
        #     y_axis.append(item[1])

        # x = min(y_axis)










        return p0

s = Solution()
print(s.outerTrees(trees=[[1,1], [2,2], [2,0], [2,4], [3,3], [4,2]]))