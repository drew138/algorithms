# problem: https://leetcode.com/problems/sqrtx/submissions/
# Runtime: 36 ms, faster than 54.92% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.4 MB, less than 7.19% of Python3 online submissions for Sqrt(x).

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, (x // 2) + 1

        while left < right:
            mid = left + ((right - left) // 2) + 1
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        if mid ** 2 > x:
            mid -= 1
        return mid
