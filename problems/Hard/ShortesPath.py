from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if k >= rows + cols - 2:
            return rows + cols - 2
        target = (rows - 1, cols - 1)
        startState = (0, 0, k)
        seen = set(startState)

        que = deque()
        que.append((startState, 0))

        while que:
            (row, col, k), steps = que.popleft()
            if (row, col) == target:
                return steps

            for nbr in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nrow, ncol = row + nbr[0], col + nbr[1]

                if 0 <= nrow < rows and 0 <= ncol < cols:
                    newK = k - grid[nrow][ncol]
                    if newK >= 0 and (nrow, ncol, newK) not in seen:
                        seen.add((nrow, ncol, newK))
                        que.append(((nrow, ncol, newK), steps + 1))

        return -1