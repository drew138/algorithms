# problem: https://leetcode.com/problems/valid-number/
# Runtime: 32 ms, faster than 78.17% of Python3 online submissions for Valid Number.
# Memory Usage: 14.4 MB, less than 30.07% of Python3 online submissions for Valid Number.

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r"^[-+)]?(([0-9]+\.?[0-9]*)|([0-9]*\.[0-9]+))([eE][-+]?[0-9]+)?$", s)
