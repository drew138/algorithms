# problem: https://leetcode.com/problems/baseball-game/
# Runtime: 53 ms, faster than 61.51% of Python3 online submissions for Baseball Game.
# Memory Usage: 14 MB, less than 95.48% of Python3 online submissions for Baseball Game.

from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops:
            if op == '+':
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                scores.append(scores[-1] * 2)
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)