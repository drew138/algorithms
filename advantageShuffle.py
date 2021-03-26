# problem: https://leetcode.com/problems/advantage-shuffle/
# Runtime: 356 ms, faster than 65.78% of Python3 online submissions for Advantage Shuffle.
# Memory Usage: 17.4 MB, less than 62.22% of Python3 online submissions for Advantage Shuffle.

from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        from collections import defaultdict

        A.sort()
        cp = B.copy()
        cp.sort()
        m = defaultdict(list)
        i, j = 0, 0
        res = []
        prov = []
        while i < len(A):
            if A[i] > cp[j]:
                m[cp[j]].append(A[i])
                j += 1
            else:
                prov.append(A[i])
            i += 1
        for num in B:
            res.append(m[num].pop() if m[num] else prov.pop())
        return res
