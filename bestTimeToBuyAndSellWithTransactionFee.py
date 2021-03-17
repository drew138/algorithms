# problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# Runtime: 672 ms, faster than 89.40% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
# Memory Usage: 21.4 MB, less than 55.43% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell, buy = 0, -prices[0]
        for price in prices:
            sell = max(sell, buy + price - fee)
            buy = max(buy, sell - price)
        return sell
