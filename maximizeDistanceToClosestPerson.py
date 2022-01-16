# problem: https://leetcode.com/problems/maximize-distance-to-closest-person/
# Runtime: 128 ms, faster than 89.20% of Python3 online submissions for Maximize Distance to Closest Person.
# Memory Usage: 14.6 MB, less than 92.48% of Python3 online submissions for Maximize Distance to Closest Person.

import math
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        cur = 0
        sol = 0
        start, end = True, True
        for seat in seats:
            if seat == 0:
                end = True
                cur += 1
            else:
                if start:
                    sol = max(sol, cur)
                else:
                    sol = max(sol, math.ceil(cur / 2))
                
                start = False
                end = False
                cur = 0
        if (start and end) or end:
            sol = max(sol, cur)
        return sol
