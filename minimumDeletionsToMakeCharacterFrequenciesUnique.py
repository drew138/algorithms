# problem: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# Runtime: 290 ms, faster than 44.27% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# Memory Usage: 15.3 MB, less than 5.13% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.

from collections import Counter
from sortedcontainers import SortedList
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        sl = SortedList(counter.values())
        ans = 0
        while sl and len(sl) >= 2:
            first = sl.pop(-1)
            second = sl.pop(-1)
            if first == second == 0:
                continue
            if first == second:
                sl.add(first)
                
                sl.add(second - 1)
                ans += 1
            else:
                sl.add(second)
        return ans