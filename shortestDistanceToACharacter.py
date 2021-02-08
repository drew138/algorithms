# problem :https://leetcode.com/problems/shortest-distance-to-a-character/
# Runtime: 44 ms, faster than 61.83% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 14.6 MB, less than 6.38% of Python3 online submissions for Shortest Distance to a Character.

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dp = []
        for a in s:
            if a == c:
                dp.append(0)
            else:
                dp.append(float("inf"))
        prev = s.index(c)
        for i in range(prev+1, len(s)):
            if s[i] == c:
                prev = i
            dp[i] = min(abs(i-prev), dp[i])
        for i in range(len(dp) - 1, -1, -1):
            if s[i] == c:
                prev = i
            dp[i] = min(abs(i-prev), dp[i])
        return dp
