# problem: https: // leetcode.com/problems/pacific-atlantic-water-flow/submissions/
# Runtime: 2164 ms, faster than 8.62 % of Python3 online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15.5 MB, less than 22.06 % of Python3 online submissions for Pacific Atlantic Water Flow.
from typing import List


class Solution:
    def getConnections(self, cell):
        x, y = cell
        connections = []
        if x > 0:
            connections.append((x-1, y))
        if x < self.height:
            connections.append((x+1, y))
        if y > 0:
            connections.append((x, y-1))
        if y < self.width:
            connections.append((x, y + 1))
        return connections

    def bfs(self, i, j):
        from collections import deque
        reachPacific = i == 0 or j == 0
        reachAtlantic = i == self.height or j == self.width
        if reachPacific and reachAtlantic:
            self.answer.add((i, j))
            return
        queue = deque()
        for cell in self.getConnections((i, j)):
            x, y = cell
            if self.matrix[i][j] >= self.matrix[x][y]:
                if cell in self.answer:
                    self.answer.add((i, j))
                    return
                queue.append(cell)
        while queue:
            cell = queue.popleft()
            m, n = cell
            reachPacific = reachPacific or (m == 0 or n == 0)
            reachAtlantic = reachAtlantic or (
                m == self.height or n == self.width)
            if (reachPacific and reachAtlantic):
                self.answer.add((i, j))
                return
            for c in self.getConnections(cell):
                x, y = c
                if self.matrix[m][n] >= self.matrix[x][y] and not c in self.visited:
                    if c in self.answer:
                        self.answer.add((i, j))
                        return
                    queue.append(c)
                    self.visited.add(c)

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return matrix
        self.height = len(matrix) - 1
        self.width = len(matrix[0]) - 1
        self.matrix = matrix
        self.answer = set()
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                self.visited = set()
                self.visited.add((i, j))
                self.bfs(i, j)
        return list(self.answer)
