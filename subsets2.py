# problem: https://leetcode.com/problems/subsets-ii/
# Runtime: 36 ms, faster than 77.71% of Python3 online submissions for Subsets II.
# Memory Usage: 14.3 MB, less than 82.75% of Python3 online submissions for Subsets II.


from typing import List


class Solution:
    def dfs(self, i, stack):
        self.answer.add(tuple(sorted(stack)))
        for j in range(i, len(self.nums)):
            stack.append(self.nums[j])
            self.dfs(j+1, stack)
            stack.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.answer = set()
        self.answer.add(tuple([]))
        self.nums = nums
        stack = []
        for i in range(len(nums)):
            stack.append(self.nums[i])
            self.dfs(i+1, stack)
            stack.pop()
        return list(self.answer)
