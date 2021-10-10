# problem: https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Runtime: 56 ms, faster than 82.71% of Python3 online submissions for Bitwise AND of Numbers Range.
# Memory Usage: 14.2 MB, less than 55.95% of Python3 online submissions for Bitwise AND of Numbers Range.

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        answer = 0
        i = 0
        while right:
            cur_left = left & 1
            cur_right = right & 1
            left >>= 1
            right >>= 1
            if cur_left != cur_right:
                answer = 0
            answer = (cur_left << i) | answer
            i += 1
        return answer
