# problem: https://leetcode.com/problems/range-addition-ii/submissions/
# Runtime: 86 ms, faster than 10.56% of Python3 online submissions for Range Addition II.
# Memory Usage: 16.2 MB, less than 21.88% of Python3 online submissions for Range Addition II.

from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x, y = m, n
        for i, j in ops:
            x, y = min(x, i), min(y, j)
        return x * y
