# problem: https://leetcode.com/problems/zigzag-conversion/
# Runtime: 68 ms, faster than 51.10% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 14.3 MB, less than 87.30% of Python3 online submissions for ZigZag Conversion.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = []
        if numRows == 1:
            return s

        leap = 2 * (numRows) - 2

        def increment(i, leap_left, leap_right, left):
            if i == 0 or i == numRows - 1:
                return leap
            return leap_left if left else leap_right

        for i in range(numRows):
            j = i
            leap_left = 2 * (numRows - j) - 2
            leap_right = leap - leap_left
            left = True
            while j < len(s):
                answer.append(s[j])
                j += increment(i, leap_left, leap_right, left)
                left = not left

        return "".join(answer)
