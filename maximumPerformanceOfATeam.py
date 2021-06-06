# problem: https: // leetcode.com/problems/maximum-performance-of-a-team/
# Runtime: 392 ms, faster than 55.17 % of Python3 online submissions for Maximum Performance of a Team.
# Memory Usage: 29.9 MB, less than 86.21 % of Python3 online submissions for Maximum Performance of a Team.

from typing import List
from heapq import heappush, heappop


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        answer = 0
        l = sorted(zip(efficiency, speed), reverse=True)
        total = 0
        for e, s in l:
            if len(heap) > k - 1:
                total -= heappop(heap)
            heappush(heap, s)
            total += s
            answer = max(answer, total*e)

        return answer % (10**9 + 7)
