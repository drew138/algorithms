# problem: https://leetcode.com/problems/merge-intervals/submissions/
# Runtime: 76 ms, faster than 95.96% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.8 MB, less than 27.19% of Python3 online submissions for Merge Intervals.

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i, j, lenArr = 0, 1, len(intervals)
        if lenArr == 1:
            return intervals
        answer = []
        while j < lenArr:
            if intervals[i][1] >= intervals[j][1]:
                if j == (lenArr - 1):
                    answer.append(intervals[i])
                j += 1
            elif intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = intervals[j][1]
                if j == (lenArr - 1):
                    answer.append(intervals[i])
                j += 1
            elif intervals[i][1] < intervals[j][0]:
                answer.append(intervals[i])
                i = j
                if j == (lenArr - 1):
                    answer.append(intervals[j])
                j += 1

        return answer
