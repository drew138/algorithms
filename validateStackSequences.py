# problem: https://leetcode.com/problems/validate-stack-sequences/
# Runtime: 68 ms, faster than 84.35% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.4 MB, less than 85.37% of Python3 online submissions for Validate Stack Sequences.

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped.reverse()
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and popped and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
        return not popped
