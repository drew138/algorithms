# problem: https://leetcode.com/problems/partition-labels/
# Runtime: 141 ms, faster than 5.04% of Python3 online submissions for Partition Labels.
# Memory Usage: 14 MB, less than 36.30% of Python3 online submissions for Partition Labels.


from collections import Counter, defaultdict
from typing import List


class Solution:
    def check(self, cur, counter):
        for key, val in cur.items():
            if val !=  counter[key]:
                return False
        return cur

    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        sol = []
        cur = defaultdict(int)
        prev = 0
        n = len(s)
        for i, character in enumerate(s):
            if self.check(cur, counter):
                sol.append(i - prev)
                prev = i
            cur[character] += 1
        if self.check(cur, counter):
                sol.append(n - prev)   
        return sol
