# problem: https://leetcode.com/problems/generate-parentheses/
# Runtime: 36 ms, faster than 65.90% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.6 MB, less than 36.63% of Python3 online submissions for Generate Parentheses.

from typing import List


class Solution:
    def traverse(self, stack, opening, closing):
        if not opening and not closing:
            self.answer.append("".join(stack))
        if opening:
            stack.append("(")
            self.traverse(stack, opening - 1, closing + 1)
            stack.pop()
        if closing:
            stack.append(")")
            self.traverse(stack, opening, closing - 1)
            stack.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        self.traverse([], n, 0)
        return self.answer
