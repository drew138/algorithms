# problem: https://leetcode.com/problems/course-schedule-ii/
# Runtime: 92 ms, faster than 94.59% of Python3 online submissions for Course Schedule II.
# Memory Usage: 16.6 MB, less than 43.62% of Python3 online submissions for Course Schedule II.

from typing import List


class Solution:
    
    def dfs(self, node, adjacency, answer, visited):
        if visited[node] == -1:
            self.can_be_completed = False
            return
        elif visited[node] == 1 or not self.can_be_completed:
            return
        visited[node] = -1
        for connection in adjacency[node]:
            if visited[connection] != 1:
                self.dfs(connection, adjacency, answer, visited)
        answer.append(node)
        visited[node] = 1
    
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        visited = numCourses * [0]
        adjacency = defaultdict(list)
        for to_node, from_node in prerequisites:
            adjacency[from_node].append(to_node)
        answer = []
        self.can_be_completed = True
        for i in range(numCourses):
            self.dfs(i, adjacency, answer, visited)
        if not self.can_be_completed:
            return []
        answer.reverse()
        return answer