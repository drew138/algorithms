# problem: https://leetcode.com/problems/find-the-most-competitive-subsequence/submissions/
# Runtime: 1272 ms, faster than 50.00% of Python3 online submissions for Find the Most Competitive Subsequence.
# Memory Usage: 27.2 MB, less than 50.00% of Python3 online submissions for Find the Most Competitive Subsequence.

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        index = 0
        for i in range(len(nums) - k + 1):
            if nums[i] < nums[index]:
                index = i
        stack = []
        for i in range(index, len(nums)):
            while stack and stack[-1] > nums[i] and (len(stack) + len(nums) - i > k):
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
            if len(stack) + len(nums) - i == k:
                stack += nums[i+1:]
                break
        return stack
