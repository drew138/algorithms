# problem: https://leetcode.com/problems/three-equal-parts/
# Runtime: 676 ms, faster than 29.03% of Python3 online submissions for Three Equal Parts.
# Memory Usage: 15.1 MB, less than 88.17% of Python3 online submissions for Three Equal Parts.


from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n < 3 or sum(arr) % 3:
            return [-1, -1]
        a, b, c = arr[0], arr[1], arr[2]
        for i in range(3, n):
            c <<= 1
            c |= arr[i]
        i, j = 0, 2
        if a == b == c:
            return [i, j]
        while a < b or b < c:
            if a < b and i + 2 < j:
                i += 1
                b ^= arr[i] << (j-i-1)
                a <<= 1
                a |= arr[i]
            elif b < c and j + 1 < n:
                c ^= arr[j] << (n-j-1)
                b <<= 1
                b |= arr[j]
                j += 1
            if a == b == c:
                return [i, j]
        return [-1, -1]
