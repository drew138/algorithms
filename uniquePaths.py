# problem: https://leetcode.com/problems/unique-paths/
# Runtime: 32 ms, faster than 69.60% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.1 MB, less than 96.34% of Python3 online submissions for Unique Paths.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
