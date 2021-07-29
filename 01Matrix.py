# problem: https://leetcode.com/problems/01-matrix/
# Runtime: 780 ms, faster than 44.30% of Python3 online submissions for 01 Matrix.
# Memory Usage: 17.6 MB, less than 27.16% of Python3 online submissions for 01 Matrix.

from typing import List


class Solution:

    dirs = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    )

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        zeros = [
            (i, j) for i in range(len(mat))
            for j in range(len(mat[0])) if not mat[i][j]
        ]
        visited = set(zeros)
        queue = deque(zeros)
        layer = 0
        while queue:

            layer += 1
            tmp = deque()
            while queue:
                x, y = queue.popleft()
                for a, b in self.dirs:
                    if 0 <= x + a < len(mat) and 0 <= y + b < len(mat[0]) and not (x + a, y + b) in visited:
                        visited.add((x + a, y + b))
                        mat[x+a][y+b] = layer
                        tmp.append((x+a, y+b))
            queue = tmp
        return mat
