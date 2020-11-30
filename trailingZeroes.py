# problem: https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
# Runtime: 24 ms, faster than 95.76% of Python3 online submissions for Factorial Trailing Zeroes.
# Memory Usage: 14 MB, less than 81.88% of Python3 online submissions for Factorial Trailing Zeroes.


class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0
        while n:
            answer += n//5
            n //= 5
        return answer
