# problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Runtime: 44 ms, faster than 53.53% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
# Memory Usage: 14.9 MB, less than 18.99% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][1] -= prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = dp[i-1][1] + prices[i]
        return max(dp[-1])
