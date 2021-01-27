# problem: https://leetcode.com/problems/path-with-minimum-effort/
# Runtime: 1428 ms, faster than 28.78% of Python3 online submissions for Path With Minimum Effort.
# Memory Usage: 16.1 MB, less than 49.74% of Python3 online submissions for Path With Minimum Effort.

from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        from sortedcontainers import SortedList
        m = len(heights)
        n = len(heights[0])
        arr = [[float("inf") for _ in range(n)] for _ in range(m)]
        pqueue = SortedList([[0, 0, 0]], key=lambda x: x[0])
        while pqueue:
            dist, row, col = pqueue.pop(index=0)
            if dist > arr[row][col]:
                continue
            if row == m-1 and col == n-1:
                return dist
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= row + d[0] < m and 0 <= col + d[1] < n:
                    newDist = max(
                        dist, abs(heights[row+d[0]][col+d[1]] - heights[row][col]))
                    if newDist < arr[row+d[0]][col+d[1]]:
                        arr[row+d[0]][col+d[1]] = newDist
                        pqueue.add([newDist, row+d[0], col+d[1]])
        return 0
