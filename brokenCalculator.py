# problem: https://leetcode.com/problems/broken-calculator/
# Runtime: 32 ms, faster than 57.14% of Python3 online submissions for Broken Calculator.
# Memory Usage: 14.3 MB, less than 47.18% of Python3 online submissions for Broken Calculator.


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        answer = 0
        while Y > X:
            answer += 1
            if Y % 2 == 0:
                Y /= 2
            else:
                Y += 1
        return int(answer + (X - Y))
