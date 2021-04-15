# problem: https: // leetcode.com/problems/fibonacci-number/
# Runtime: 32 ms, faster than 60.47% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14.3 MB, less than 41.55% of Python3 online submissions for Fibonacci Number.

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        prev = 0
        cur = 1
        for _ in range(2, n+1):
            prev, cur = cur, prev + cur
        return cur
