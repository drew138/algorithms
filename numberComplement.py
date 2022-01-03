# problem: https://leetcode.com/problems/number-complement/submissions/ 
# Runtime: 28 ms, faster than 81.72% of Python3 online submissions for Number Complement.
# Memory Usage: 14.1 MB, less than 68.47% of Python3 online submissions for Number Complement.


class Solution:
    def findComplement(self, num: int) -> int:
        n = 0
        tmp = num
        answer = 0
        while tmp:
            digit = 0 if tmp & 1 else 1
            tmp >>= 1
            answer = answer | (digit << n)
            n += 1
        return answer