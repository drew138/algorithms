# problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Runtime: 60 ms, faster than 92.42% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 14.7 MB, less than 42.12% of Python3 online submissions for Evaluate Reverse Polish Notation.

from typing import List
from math import ceil


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token.lstrip("-").isnumeric():
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "*":
                    res = b * a
                elif token == "/":
                    res = b // a if b / a > 0 else ceil(b / a)
                elif token == "+":
                    res = b + a
                else:
                    res = b - a
                stack.append(res)
        return stack[0]
