# problem: https://leetcode.com/problems/can-convert-string-in-k-moves/
# Runtime: 664 ms, faster than 5.83% of Python3 online submissions for Can Convert String in K Moves.
# Memory Usage: 15 MB, less than 91.75% of Python3 online submissions for Can Convert String in K Moves.

class Solution:
    def aux(self, x):
        if x[0] > x[1]:
            return 26 - x[0] + x[1]
        else:
            return x[1] - x[0]

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False
        m = defaultdict(int)
        for a, b in zip(s, t):
            m[self.aux((ord(a), ord(b)))] += 1
        m[0] = 0
        for i in range(1, 27):
            tmp = i % 26
            if m[tmp]:
                m[tmp] -= min(k // 26 + 1, m[tmp]
                              ) if k % 26 >= i else min(k // 26, m[tmp])
        return not any(list(m.values()))
