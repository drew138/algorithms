# problem: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
# Runtime: 67 ms, faster than 6.02% of Python3 online submissions for Minimum Swaps to Make Strings Equal.
# Memory Usage: 14.3 MB, less than 23.49% of Python3 online submissions for Minimum Swaps to Make Strings Equal.

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        from collections import defaultdict
        c = defaultdict(int)
        for x, y in zip(s1, s2):
            if x != y:
                c[x] += 1
        if (c['x'] + c['y']) & 1:
            return -1
        
        return c['x'] // 2 + c['y'] // 2 + (c['x'] % 2 + c['y'] % 2)
        