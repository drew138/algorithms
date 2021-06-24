# problem: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
# Runtime: 3876 ms, faster than 60.31% of Python3 online submissions for Minimum Speed to Arrive on Time.
# Memory Usage: 28.3 MB, less than 79.15% of Python3 online submissions for Minimum Speed to Arrive on Time.

from typing import List
import math


class Solution:

    def aux(self, dist, speed):
        return sum([math.ceil(d / speed) for d in dist[:-1]]) + (dist[-1]/speed)

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l, h = 1, 10**7

        while l < h:
            mid = ((h - l) // 2) + l
            if self.aux(dist, mid) > hour:
                l = mid + 1
            else:
                h = mid
        if self.aux(dist, h) > hour:
            return -1
        return h
