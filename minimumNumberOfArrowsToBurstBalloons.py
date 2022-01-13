# problem: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Runtime: 1885 ms, faster than 25.16% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
# Memory Usage: 59.1 MB, less than 35.42% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = -float("inf")
        sol = 0
        for start, end in points:
            if start > prev:
                sol += 1
                prev = end
            else:
                prev = min(prev, end)
        return sol