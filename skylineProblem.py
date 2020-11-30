# problem: https://leetcode.com/problems/the-skyline-problem/
# Runtime: 148 ms, faster than 34.21% of Python3 online submissions for The Skyline Problem.
# Memory Usage: 21 MB, less than 8.98% of Python3 online submissions for The Skyline Problem.
from typing import List


class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        from sortedcontainers import SortedList
        points = []
        answer = []
        for coord in buildings:
            points.append([coord[0], coord[-1], "s"])
            points.append([coord[1], coord[-1], "e"])
        points.sort(key=lambda x: (x[0], -x[1] if x[2] == 's' else x[1]))
        priority_queue = SortedList([0])
        max_height = 0
        for point in points:
            prev = max_height
            if point[-1] == "s":
                priority_queue.add(point[1])
                max_height = priority_queue[-1]
                if max_height > prev:
                    answer.append(point[:2])
            else:
                priority_queue.remove(point[1])
                max_height = priority_queue[-1]
                if prev > max_height:
                    answer.append([point[0], max_height])
        return answer
