# problem: https://leetcode.com/problems/course-schedule-iii/
# Runtime: 692 ms, faster than 77.74% of Python3 online submissions for Course Schedule III.
# Memory Usage: 19.3 MB, less than 90.65% of Python3 online submissions for Course Schedule III.

from typing import List

import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses.sort(key=lambda x: x[1])
        heap, dur = [], 0
        for time, end in courses:
            dur += time
            heapq.heappush(heap, -time)
            if dur > end:
                dur += heapq.heappop(heap)
        return len(heap)
