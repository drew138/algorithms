# problem: https://leetcode.com/problems/n-th-tribonacci-number/
# Runtime: 32 ms, faster than 63.56% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 14.1 MB, less than 69.95% of Python3 online submissions for N-th Tribonacci Number.

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        first, second, third = 0, 1, 1
        for i in range(3, n+1):
            first, second, third = second, third, first + second + third
        return third
