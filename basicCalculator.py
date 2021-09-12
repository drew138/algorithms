# problem: https://leetcode.com/problems/basic-calculator/
# Runtime: 224 ms, faster than 7.87% of Python3 online submissions for Basic Calculator.
# Memory Usage: 15.5 MB, less than 96.65% of Python3 online submissions for Basic Calculator.

class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        i = 0
        while i < len(s):
            while len(stack) >= 2:
                if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 + num2)
                elif isinstance(stack[-1], int) and stack[-2] == "-":
                    num = stack.pop()
                    stack.pop()
                    stack.append(-num)
                else:
                    break
            character = s[i]
            if character == "(":
                stack.append("(")
            elif character == ")":
                num = stack.pop()
                stack.pop()
                stack.append(num)
            elif character == "-":
                stack.append("-")
            elif character.isnumeric():
                j = i
                while i < len(s) and s[i].isnumeric():
                    i += 1
                if i == j:
                    j = i + 1
                    i += 1
                stack.append(int(s[j:i]))
                continue
            i += 1
        while len(stack) >= 2:
            if isinstance(stack[-1], int) and isinstance(stack[-2], int):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif isinstance(stack[-1], int) and stack[-2] == "-":
                num = stack.pop()
                stack.pop()
                stack.append(-num)
            else:
                break
        return stack[0]
