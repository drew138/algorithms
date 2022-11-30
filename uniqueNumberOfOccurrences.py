# problem: https://leetcode.com/problems/unique-number-of-occurrences/
# Runtime: 58 ms, faster than 72.14% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 14 MB, less than 72.74% of Python3 online submissions for Unique Number of Occurrences.

from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return all([el == 1 for el in Counter(Counter(arr).values()).values()])
