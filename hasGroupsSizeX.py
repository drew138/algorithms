# problem: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/submissions/
# Runtime: 132 ms, faster than 54.77% of Python3 online submissions for X of a Kind in a Deck of Cards.
# Memory Usage: 14.6 MB, less than 13.74% of Python3 online submissions for X of a Kind in a Deck of Cards.

from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import defaultdict
        from math import gcd
        m = defaultdict(int)
        for card in deck:
            m[card] += 1
        vals = [m[key] for key in m]
        div = gcd(*vals)
        return div > 1
