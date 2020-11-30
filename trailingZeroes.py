# problem: https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
# Runtime: 124 ms, faster than 33.28% of Python3 online submissions for Factorial Trailing Zeroes.
# Memory Usage: 14 MB, less than 96.37% of Python3 online submissions for Factorial Trailing Zeroes.


class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0
        for i in range(0, n + 1, 5):
            x = i
            while (x % 5 == 0) and x != 0:
                x /= 5
                answer += 1
        return answer
