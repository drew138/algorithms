# problem: https://leetcode.com/problems/max-area-of-island/
# Runtime: 144 ms, faster than 54.04% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.7 MB, less than 82.14% of Python3 online submissions for Max Area of Island.


from typing import List


class Solution:
    def bfs(self, grid, visited, coord):
        from collections import deque
        dirs = ((-1, 0), (0, -1), (0, 1), (1, 0))
        queue = deque()
        queue.append(coord)
        biggest_island = 0
        while queue:
            x, y = queue.popleft()
            biggest_island += 1
            for a, b in dirs:
                if 0 <= a + x < len(grid) and 0 <= b + y < len(grid[0]) and grid[a + x][b + y] and not (a + x, b + y) in visited:
                    visited.add((a + x, b + y))
                    queue.append((a + x, b + y))
        return biggest_island

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and not (i, j) in visited:
                    visited.add((i, j))
                    answer = max(self.bfs(grid, visited, (i, j)), answer)
        return answer
