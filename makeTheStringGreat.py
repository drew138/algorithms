# problem: https://leetcode.com/problems/make-the-string-great/
# Runtime: 35 ms, faster than 96.38% of Python3 online submissions for Make The String Great.
# Memory Usage: 13.9 MB, less than 61.84% of Python3 online submissions for Make The String Great.

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            cond_one = c.isupper(
            ) and stack and stack[-1].islower() and c.lower() == stack[-1]
            cond_two = c.islower(
            ) and stack and stack[-1].isupper() and c.upper() == stack[-1]
            if cond_one or cond_two:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
