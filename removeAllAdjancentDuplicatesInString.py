# problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Runtime: 72 ms, faster than 64.82% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.8 MB, less than 22.34% of Python3 online submissions for Remove All Adjacent Duplicates In String.


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
