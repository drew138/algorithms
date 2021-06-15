# problem: https://leetcode.com/problems/matchsticks-to-square/
# Runtime: 1064 ms, faster than 44.77% of Python3 online submissions for Matchsticks to Square.
# Memory Usage: 14.1 MB, less than 90.35% of Python3 online submissions for Matchsticks to Square.

from typing import List

from functools import lru_cache


class Solution:

    @lru_cache(None)
    def traverse(self, i, l1, l2, l3, l4, side):
        if i < 0 and l1 == l2 == l3 == l4 == side:
            self.canBeFormed = True
            return
        if not self.canBeFormed and i >= 0:
            n = self.matchsticks[i]
            if l1 + n <= side:
                self.traverse(i - 1, l1 + n, l2, l3, l4, side)
            if l2 + n <= side:
                self.traverse(i - 1, l1, l2 + n, l3, l4, side)
            if l3 + n <= side:
                self.traverse(i - 1, l1, l2, l3 + n, l4, side)
            if l4 + n <= side:
                self.traverse(i - 1, l1, l2, l3, l4 + n, side)

    def makesquare(self, matchsticks: List[int]) -> bool:
        side = sum(matchsticks) / 4
        if side % 1:
            return False
        self.canBeFormed = False
        self.matchsticks = matchsticks
        self.matchsticks.sort()
        self.traverse(len(matchsticks) - 1, 0, 0, 0, 0, side)
        return self.canBeFormed
