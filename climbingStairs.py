# problem: https://leetcode.com/problems/climbing-stairs/
# Runtime: 45 ms, faster than 17.22% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14.4 MB, less than 11.04% of Python3 online submissions for Climbing Stairs.


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(n + 1):
            for j in range(1, 3):
                if i - j >= 0:
                    dp[i] += dp[i-j]
        return dp[-1]
