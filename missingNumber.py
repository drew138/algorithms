# problem: https://leetcode.com/problems/missing-number/
# Runtime: 124 ms, faster than 91.29% of Python3 online submissions for Missing Number.
# Memory Usage: 15.4 MB, less than 82.71% of Python3 online submissions for Missing Number.

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int((n*(n+1))/2 - sum(nums))
