# problem: https://leetcode.com/problems/4sum-ii/submissions/
# Runtime: 276 ms, faster than 65.82% of Python3 online submissions for 4Sum II.
# Memory Usage: 55.7 MB, less than 31.57% of Python3 online submissions for 4Sum II.
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import defaultdict
        results = defaultdict(int)
        answer = 0
        for num in A:
            for numTwo in B:
                results[-(numTwo + num)] += 1
        for num in C:
            for numTwo in D:
                if results[num + numTwo]:
                    answer += results[num + numTwo]
        return answer
