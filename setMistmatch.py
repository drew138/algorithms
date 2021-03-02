# problem: https://leetcode.com/problems/set-mismatch/
# Runtime: 192 ms, faster than 74.92% of Python3 online submissions for Set Mismatch.
# Memory Usage: 15.2 MB, less than 98.51% of Python3 online submissions for Set Mismatch.

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A = -sum(nums) + n*(n+1)//2
        B = -sum(i*i for i in nums) + n*(n+1)*(2*n+1)//6
        return [int((B/A - A)/2), int((B/A + A)//2)]
