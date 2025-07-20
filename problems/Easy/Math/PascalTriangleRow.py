from typing import List


class Solution:
    def generate(self, numRows: int) -> List[int]:
        ans = [[1] * i for i in range(1, numRows+2)]
        for i in range(2, numRows+1):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]

        return  ans[numRows]


s = Solution()
print(s.generate(numRows=100))