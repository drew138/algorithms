# problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Runtime: 32 ms, faster than 63.53% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 14.2 MB, less than 39.48% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num = num // 2 + num % 2
            steps += 1
        return steps
