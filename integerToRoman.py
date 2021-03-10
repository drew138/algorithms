# problem: https://leetcode.com/problems/integer-to-roman/
# Runtime: 48 ms, faster than 75.14% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.2 MB, less than 86.07% of Python3 online submissions for Integer to Roman.

class Solution:
    def intToRoman(self, num: int) -> str:
        answer = []
        while num:
            if num >= 1000:
                answer.append("M")
                num -= 1000
            elif num >= 900:
                answer.append('CM')
                num -= 900
            elif num >= 500:
                answer.append("D")
                num -= 500
            elif num >= 400:
                answer.append("CD")
                num -= 400
            elif num >= 100:
                answer.append("C")
                num -= 100
            elif num >= 90:
                answer.append("XC")
                num -= 90
            elif num >= 50:
                answer.append("L")
                num -= 50
            elif num >= 40:
                answer.append("XL")
                num -= 40
            elif num >= 10:
                answer.append("X")
                num -= 10
            elif num >= 9:
                answer.append("IX")
                num -= 9
            elif num >= 5:
                answer.append("V")
                num -= 5
            elif num >= 4:
                answer.append("IV")
                num -= 4
            elif num >= 1:
                answer.append("I")
                num -= 1
        return "".join(answer)
