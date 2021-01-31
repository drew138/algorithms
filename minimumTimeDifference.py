# problem: https: // leetcode.com/problems/minimum-time-difference/
# Runtime: 108 ms, faster than 11.45% of Python3 online submissions for Minimum Time Difference.
# Memory Usage: 17 MB, less than 74.34% of Python3 online submissions for Minimum Time Difference.

from typing import List


class Solution:
    def toMinutes(self, timestamp):
        t = timestamp.split(":")
        return (int(t[0]) * 60) + int(t[1])

    def findMinDifference(self, timePoints: List[str]) -> int:
        timestamps = [False] * (24*60)
        if 60*24 < len(timePoints):   # Pigeonhole theory
            return 0
        for i in range(len(timePoints)):
            position = self.toMinutes(timePoints[i])
            if timestamps[position]:
                return 0
            timestamps[position] = True
        answer = float("inf")
        prev = timestamps.index(True)
        first = prev
        for i in range(prev + 1, len(timestamps)):
            if timestamps[i]:
                answer = min(answer, i - prev)
                prev = i
        answer = min(answer, (60 * 24 - prev) + (first - 0))
        return answer
