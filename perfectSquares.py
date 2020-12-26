# problem: https://leetcode.com/problems/perfect-squares/
# Runtime: 5572 ms, faster than 15.49% of Python3 online submissions for Perfect Squares.
# Memory Usage: 14.3 MB, less than 78.57% of Python3 online submissions for Perfect Squares.

class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares = [x ** 2 for x in range(1, n+1) if x**2 <= n]
        change = [n+1] * (n+1)
        change[0] = 0
        for i in range(n+1):
            for j in range(len(perfectSquares)):
                if perfectSquares[j] <= i:
                    change[i] = min(
                        change[i], 1 + change[i - perfectSquares[j]])
        return change[-1]
