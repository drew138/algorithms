# problem: https://leetcode.com/problems/score-of-parentheses/
# Runtime: 32 ms, faster than 56.58% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14.2 MB, less than 73.28% of Python3 online submissions for Score of Parentheses.


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        answer = 0
        for c in S:
            if c == "(":
                stack.append(answer)
                answer = 0
            else:
                answer = stack.pop() + max(answer * 2, 1)
            print(stack, answer)
        return answer
