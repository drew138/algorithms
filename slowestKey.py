# problem: https://leetcode.com/problems/slowest-key/
# Runtime: 60 ms, faster than 42.29% of Python3 online submissions for Slowest Key.
# Memory Usage: 14.4 MB, less than 56.84% of Python3 online submissions for Slowest Key.

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        from collections import defaultdict
        count = defaultdict(int)
        prev = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            releaseTimes[i], prev = releaseTimes[i] - prev, releaseTimes[i]
        maxVal = 0
        for time, key in zip(releaseTimes, keysPressed):
            count[key] = max(time, count[key])
            maxVal = max(maxVal, count[key])
        vals = sorted([key for key in count.keys() if count[key] == maxVal])
        return vals[-1]
