from typing import List


class Solution:
    def find_ball(self, grid: List[List[int]]) -> List[int]:
        rows, column = len(grid), len(grid[0])

        def check_ball(row, col):
            if row == rows:
                return col

            next_col = col + grid[row][col]

            if next_col == column or next_col == -1 or grid[row][next_col] != grid[row][col]:
                return -1
            else:
                return check_ball(row+1, next_col)

        result = []
        for i in range(column):
            result.append(check_ball(0, i))
        return result


s = Solution()
print(s.find_ball(grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
