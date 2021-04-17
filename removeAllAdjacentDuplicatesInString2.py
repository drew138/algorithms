# problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# Runtime: 108 ms, faster than 17.44% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
# Memory Usage: 19.1 MB, less than 7.20% of Python3 online submissions for Remove All Adjacent Duplicates in String II.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][1] == c:
                freq, char = stack.pop()
                if not freq + 1 == k:
                    stack.append([freq + 1, c])
            else:
                stack.append([1, c])
        return "".join([pair[0] * pair[1] for pair in stack])
