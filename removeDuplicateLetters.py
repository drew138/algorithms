# problem: https://leetcode.com/problems/remove-duplicate-letters/
# Runtime: 28 ms, faster than 99.01% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 13.8 MB, less than 99.32% of Python3 online submissions for Remove Duplicate Letters.


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}
        n = len(s)
        for i in range(n):
            last_occurrence[s[i]] = i
        stack = []
        for i, character in enumerate(s):
            if character not in stack:
                while stack and stack[-1] > character and last_occurrence[stack[-1]] > i:
                    stack.pop()       
                stack.append(character)
        return "".join(stack)
        
