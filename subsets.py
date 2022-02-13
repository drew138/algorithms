# problem: https://leetcode.com/problems/subsets/
# Runtime: 40 ms, faster than 61.13% of Python3 online submissions for Subsets.
# Memory Usage: 14 MB, less than 99.19% of Python3 online submissions for Subsets.

from typing import List

class Solution:
    def dfs(self, stack, nums, i):
        if i == len(nums):
            return
        for j in range(i + 1,len(nums)):
            stack.append(nums[j])
            self.power_set.add(tuple(stack.copy()))
            self.dfs(stack, nums, j)
            stack.pop()
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.power_set = set()
        self.dfs([], nums, -1)
        return [[]] + list(self.power_set)