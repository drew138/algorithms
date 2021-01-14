# problem: https://leetcode.com/problems/array-of-doubled-pairs/
# Runtime: 576 ms, faster than 88.17% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 16.6 MB, less than 57.71% of Python3 online submissions for Array of Doubled Pairs.

from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        from collections import Counter
        count = Counter(A)
        keys = list(count.keys())
        keys.sort()
        for key in keys:
            if count[key]:
                if count[2 * key] >= count[key]:
                    count[2 * key] -= count[key]
                    count[key] = 0
                elif count[(1/2) * key] >= count[key]:
                    count[(1/2) * key] -= count[key]
                    count[key] = 0
                else:
                    return False

        return True
