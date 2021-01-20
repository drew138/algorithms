# problem: https://leetcode.com/problems/valid-parentheses/
# Runtime: 20 ms, faster than 99.24% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.5 MB, less than 8.34% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        prev = {"(", "{", "["}
        mp = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in prev:
                stack.append(c)
            elif stack and c == mp[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
