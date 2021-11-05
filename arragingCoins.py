# problem: https://leetcode.com/problems/arranging-coins/
# Runtime: 40 ms, faster than 72.04% of Python3 online submissions for Arranging Coins.
# Memory Usage: 14.1 MB, less than 90.52% of Python3 online submissions for Arranging Coins.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left + 1 < right:
            mid = (right - left) // 2 + left
            cur = (mid * (mid + 1)) / 2
            if cur > n:
                right = mid
            else:
                left = mid
        return left
