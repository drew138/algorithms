# problem: https://leetcode.com/problems/add-strings/
# Runtime: 44 ms, faster than 56.67% of Python3 online submissions for Add Strings.
# Memory Usage: 14.4 MB, less than 39.95% of Python3 online submissions for Add Strings.

class Solution:
    def add_strings(self, a, b, carry):

        return str((int(a)+int(b)+int(carry)) // 10), str((int(a) + int(b) + int(carry)) % 10)

    def addStrings(self, num1: str, num2: str) -> str:
        carry = "0"
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        answer = []
        for i in range(max(len(num1), len(num2))):
            a = num1[i] if i < len(num1) else "0"
            b = num2[i] if i < len(num2) else "0"
            carry, num = self.add_strings(a, b, carry)
            answer.append(num)
        if carry != "0":
            answer.append(carry)
        return "".join(reversed(answer))
