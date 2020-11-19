# problem: https://leetcode.com/problems/decode-string/submissions/
# Runtime: 28 ms, faster than 70.42% of Python3 online submissions for Decode String.
# Memory Usage: 14.1 MB, less than 30.70% of Python3 online submissions for Decode String.


class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []

        answer = ""
        num = 0
        for char in s:
            if char.isnumeric():
                num = num * 10 + int(char)
            elif char == "[":
                strStack.append(answer)
                answer = ""
                numStack.append(num)
                num = 0
            elif char == "]":
                temp = answer
                answer = strStack.pop()
                count = numStack.pop()
                while count > 0:
                    answer += temp
                    count -= 1
            else:
                answer += char
        return answer
