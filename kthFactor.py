# problem: https: // leetcode.com/problems/the-kth-factor-of-n/
# Runtime: 20 ms, faster than 99.00 % of Python3 online submissions for The kth Factor of n.
# Memory Usage: 14.3 MB, less than 13.74 % of Python3 online submissions for The kth Factor of n.


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        from math import sqrt
        count = 0
        isSquare = False
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                count += 1
                last = i
                isSquare = i * i == n
            if count == k:
                return i
        count = k - count
        start = int(sqrt(n))
        if isSquare:
            start -= 1

        for i in range(start, 0, -1):
            if (n % i == 0):
                count -= 1
            if count == 0:
                return int(n / i)
        return -1
