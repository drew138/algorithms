# problem: https://leetcode.com/problems/range-sum-query-immutable/
# Runtime: 64 ms, faster than 99.31% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 17.8 MB, less than 47.09% of Python3 online submissions for Range Sum Query - Immutable.

import itertools
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):

        self.acc = list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right]-self.acc[left-1] if left > 0 else self.acc[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
