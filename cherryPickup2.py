# problem: https://leetcode.com/problems/cherry-pickup-ii/
# Runtime: 1912 ms, faster than 23.08% of Python3 online submissions for Cherry Pickup II.
# Memory Usage: 52.7 MB, less than 5.47% of Python3 online submissions for Cherry Pickup II.

from typing import List
from functools import lru_cache


class Solution:
    def getConnections(self, row, i, j):
        directions = [
            (1, -1),
            (1, 0),
            (1, 1)
        ]
        connections = []
        consI = []
        consJ = []
        for direction in directions:
            a, b = direction
            if (row + a) < len(self.grid) and 0 <= (i + b) < len(self.grid[row + a]):
                consI.append(i+b)
        for direction in directions:
            a, b = direction
            if (row + a) < len(self.grid) and 0 <= (j + b) < len(self.grid[row + a]):
                consJ.append(j+b)
        for i in range(len(consI)):
            for j in range(len(consJ)):
                connections.append((row+1, consI[i], consJ[j]))
        return connections

    @lru_cache(None)
    def traverse(self, row, i, j):
        connections = self.getConnections(row, i, j)
        cur = self.grid[row][i] + \
            self.grid[row][j] if i != j else self.grid[row][i]
        maxVal = 0
        for connection in connections:
            maxVal = max(self.traverse(*connection), maxVal)
        return maxVal + cur

    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.grid = grid
        return self.traverse(0, 0, len(grid[0]) - 1)
