# problem: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/submissions/
# Runtime: 1220 ms, faster than 100.00% of Python3 online submissions for Minimum Initial Energy to Finish Tasks.
# Memory Usage: 59.3 MB, less than 71.43% of Python3 online submissions for Minimum Initial Energy to Finish Tasks.

from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        total = 0
        for actual, _ in tasks:
            total += actual
        answer = total
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)
        dif = 0
        for actual, minimum in tasks:
            if total >= minimum:
                total -= actual
            else:
                dif = max(dif, minimum - total)
                total -= actual

        answer += dif
        return answer
