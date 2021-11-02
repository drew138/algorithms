# problem: https://leetcode.com/problems/surrounded-regions/
# Runtime: 204 ms, faster than 36.50% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 20.1 MB, less than 15.19% of Python3 online submissions for Surrounded Regions.

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict, deque
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        blobs = defaultdict(bool)
        visited = set()
        cur = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    visited.add((i, j))
                    queue = deque([(i, j)])
                    blobs[cur] = True
                    while queue:
                        x, y = queue.popleft()
                        board[x][y] = cur
                        for a, b in dirs:
                            valid = (0 <= x + a < m) and (0 <= y + b < n)
                            if valid and board[x + a][y + b] == "O" and (not (x + a, y + b) in visited):
                                queue.append((x + a, y + b))
                                visited.add((x + a, y + b))
                            elif not valid:
                                blobs[cur] = False

                    cur += 1
        for i in range(m):
            for j in range(n):
                if board[i][j] in blobs and blobs[board[i][j]]:
                    board[i][j] = "X"
                elif board[i][j] != "X":
                    board[i][j] = "O"
