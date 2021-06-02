# problem: https: // leetcode.com/problems/longest-well-performing-interval/
# Runtime: 236 ms, faster than 20.00 % of Python3 online submissions for Longest Well-Performing Interval.
# Memory Usage: 14.8 MB, less than 72.31 % of Python3 online submissions for Longest Well-Performing Interval.
from typing import List


class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        m = {}
        answer, cum = 0, 0
        for i, hour in enumerate(hours):
            cum += 1 if hour > 8 else -1
            if cum > 0:
                answer = i + 1
            elif cum - 1 in m:
                answer = max(answer, i - m[cum - 1])
            elif not cum in m:
                m[cum] = i
        return answer
