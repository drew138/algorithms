# problem:https://leetcode.com/problems/remove-covered-intervals/
# Runtime: 135 ms, faster than 51.71% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.3 MB, less than 96.04% of Python3 online submissions for Remove Covered Intervals.

from typing import List
import math

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        upper = -math.inf
        for _, hi in intervals:
            count += hi <= upper
            upper = max(hi, upper)
        return len(intervals) - count 
