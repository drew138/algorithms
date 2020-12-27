# problem: https://leetcode.com/problems/brick-wall/
# Runtime: 180 ms, faster than 63.72% of Python3 online submissions for Brick Wall.
# Memory Usage: 19.2 MB, less than 37.29% of Python3 online submissions for Brick Wall.

from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        rows = len(wall)
        edges = defaultdict(int)
        for row in wall:
            total = 0
            for i in range(len(row) - 1):
                total += row[i]
                edges[total] += 1
        maxVal = 0
        for val in edges.values():
            maxVal = max(maxVal, val)

        return rows - maxVal
