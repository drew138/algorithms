# problem: https: // leetcode.com/problems/coin-change/
# Runtime: 1296 ms, faster than 60.21 % of Python3 online submissions for Coin Change.
# Memory Usage: 14.1 MB, less than 97.76 % of Python3 online submissions for Coin Change.

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1
