# problem: https://leetcode.com/problems/k-closest-points-to-origin/
# Runtime: 668 ms, faster than 72.50% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.7 MB, less than 76.94% of Python3 online submissions for K Closest Points to Origin.

from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2) ** (1/2))
        return points[:k]