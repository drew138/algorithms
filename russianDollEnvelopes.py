# problem: https://leetcode.com/problems/russian-doll-envelopes/
# Runtime: 176 ms, faster than 42.21% of Python3 online submissions for Russian Doll Envelopes.
# Memory Usage: 16.4 MB, less than 84.16% of Python3 online submissions for Russian Doll Envelopes.

from typing import List


class Solution:
    def binSearch(self, dp, start, end, target):
        while start < end:
            mid = start + (end - start) // 2
            if dp[mid] == target:
                return mid
            elif dp[mid] > target:
                end = mid
            else:
                start = mid + 1
        return start

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        total = 0
        for i in range(len(dp)):
            idx = self.binSearch(dp, 0, total, envelopes[i][1])
            dp[idx] = envelopes[i][1]
            if idx == total:
                total += 1
        return total
