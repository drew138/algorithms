# problem: https://leetcode.com/problems/reduce-array-size-to-the-half/
# Runtime: 868 ms, faster than 10.28% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 32.5 MB, less than 42.96% of Python3 online submissions for Reduce Array Size to The Half.

from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from sortedcontainers import SortedList
        from collections import Counter
        sl = SortedList()
        n = len(arr)
        counter = Counter(arr)
        tmp = 0
        answer = 0
        for val in counter.values():
            sl.add(val)
        while tmp < n / 2:
            tmp += sl.pop()
            answer += 1
        return answer
