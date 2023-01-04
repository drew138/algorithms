# problem: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
# Runtime
# 2268 ms
# Beats
# 42.30%
# Memory
# 28.4 MB
# Beats
# 44.10%
from typing import List
from collections import Counter
from math import ceil


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        ans = 0
        for val in counter.values():
            if val == 1:
                return -1
            ans += ceil(val / 3)

        return ans
