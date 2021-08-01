# problem: https://leetcode.com/problems/making-a-large-island/
# Runtime: 4696 ms, faster than 17.18% of Python3 online submissions for Making A Large Island.
# Memory Usage: 39.7 MB, less than 32.10% of Python3 online submissions for Making A Large Island.

from typing import List


class Solution:
    dirs = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    )

    def dfs(self, i, j, cur):
        self.visited.add((i, j))
        self.grid[i][j] = cur
        total = 0
        for x, y in self.dirs:
            if (0 <= i + x < len(self.grid)) and (0 <= j + y < len(self.grid[0])) and (not (i + x, j + y) in self.visited) and self.grid[i + x][j + y]:
                total += self.dfs(i + x, j + y, cur)
        return 1 + total

    def largestIsland(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        self.grid = grid
        cur = 1
        self.visited = set()
        blob_size = defaultdict(int)
        answer = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (not (i, j) in self.visited) and (self.grid[i][j]):
                    tmp = self.dfs(i, j, cur)
                    answer = max(answer, tmp)
                    blob_size[cur] = tmp
                    cur += 1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if not self.grid[i][j]:
                    tmp = 1
                    s = set()
                    for x, y in self.dirs:
                        if 0 <= i + x < len(self.grid) and 0 <= j + y < len(self.grid) and not self.grid[i+x][j+y] in s:
                            tmp += blob_size[grid[i+x][j+y]]
                            s.add(self.grid[i+x][j+y])
                    answer = max(answer, tmp)
        return answer
