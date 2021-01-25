# problem: https://leetcode.com/problems/rotting-oranges/
# Runtime: 52 ms, faster than 69.81% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 14.4 MB, less than 39.14% of Python3 online submissions for Rotting Oranges.

from typing import List


class Solution:
    def findCoordinates(self, grid):
        rottenOranges = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenOranges += (i, j),
        return rottenOranges

    def findOrange(self, grid):
        hasOrange = False
        i = 0
        while not hasOrange and i < len(grid):
            hasOrange = 1 in grid[i]
            i += 1
        return hasOrange

    def findAdjacent(self, i, j, grid):
        positions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for position in positions:
            if 0 <= i+position[0] < len(grid) and 0 <= j+position[1] < len(grid[0]) and grid[i+position[0]][j+position[1]] == 1:
                yield i + position[0], j + position[1]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        coordinates = self.findCoordinates(grid)
        if not self.findOrange(grid):
            return 0
        queue = deque(coordinates)
        if not queue:
            return -1
        minutes = 0
        while queue:
            tmp = deque()
            print(minutes, queue)
            while queue:
                coordinate = queue.popleft()
                for c in self.findAdjacent(coordinate[0], coordinate[1], grid):
                    grid[c[0]][c[1]] = 2
                    tmp.append(c)
            queue = tmp
            minutes += 1
        if self.findOrange(grid):
            return -1
        return minutes - 1
