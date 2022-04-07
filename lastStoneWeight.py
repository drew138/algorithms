# problem: https://leetcode.com/problems/last-stone-weight/
# Runtime: 68 ms, faster than 6.38% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 14.3 MB, less than 17.07% of Python3 online submissions for Last Stone Weight.


from sortedcontainers import SortedList
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = SortedList(stones)
        while len(pq) >= 2:
            a = pq.pop(-1)
            b = pq.pop(-1)
            pq.add(a - b)
        return pq.pop()