# problem: https: // leetcode.com/problems/construct-target-array-with-multiple-sums/
# Runtime: 248 ms, faster than 84.67% of Python3 online submissions for Construct Target Array With Multiple Sums.
# Memory Usage: 20.4 MB, less than 11.68% of Python3 online submissions for Construct Target Array With Multiple Sums.

from sortedcontainers import SortedList
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:

        s = sum(target)
        sl = SortedList(target)
        print(sl)
        while sl[-1] != 1:
            val = sl.pop()
            diff = s - val
            if diff == 1:
                return True
            if diff > val or diff == 0 or val % diff == 0:
                return False
            val %= diff
            s = diff + val
            sl.add(val)
        return True
