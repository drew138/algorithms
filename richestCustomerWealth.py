# problem: https://leetcode.com/problems/richest-customer-wealth/
# Runtime: 68 ms, faster than 42.35% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14 MB, less than 96.85% of Python3 online submissions for Richest Customer Wealth.


from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max((sum(account) for account in accounts))