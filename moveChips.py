# problem: https: // leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# Runtime: 24 ms, faster than 95.57 % of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
# Memory Usage: 14.3 MB, less than 8.77 % of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.

from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even, odd = 0, 0
        for num in position:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        if even == len(position) or odd == len(position):
            return 0
        return min(even, odd)
