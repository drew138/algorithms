# problem: https://leetcode.com/problems/combination-sum/
# Runtime: 196 ms, faster than 14.67% of Python3 online submissions for Combination Sum.
# Memory Usage: 14 MB, less than 87.78% of Python3 online submissions for Combination Sum.

from typing import List


class Solution:
    def dfs(self, nums, target, i, stack):
        
        if target == 0:
            self.sol.append(stack.copy())
        
        if target < 0:
            return

        for j in range(i, len(nums)):
            stack.append(nums[j])
            self.dfs(nums, target - nums[j], j, stack)
            stack.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.sol = []
        self.dfs(candidates, target, 0, [])
        return self.sol
        