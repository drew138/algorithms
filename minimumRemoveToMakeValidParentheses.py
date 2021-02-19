# problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Runtime: 84 ms, faster than 94.25% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 16 MB, less than 68.16% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []
        for i, c in enumerate(chars):
            if c == "(":
                stack.append(i)
            elif c == ")" and stack:
                stack.pop()
            elif c == ")":
                chars[i] = ""
        for i in stack:
            chars[i] = ""
        return "".join(chars)
