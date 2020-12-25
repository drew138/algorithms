# problem: https://leetcode.com/problems/diagonal-traverse/
# Runtime: 220 ms, faster than 15.73% of Python3 online submissions for Diagonal Traverse.
# Memory Usage: 16.6 MB, less than 71.02% of Python3 online submissions for Diagonal Traverse.

from typing import List


class Solution:
    def getNext(self, i, j):
        if self.right:
            a, b = self.isInBounds(i-1, j+1)
            if a and b:
                return i-1, j+1
            else:
                self.right = False
                if b:
                    return i, j + 1
                else:
                    return i+1, j
        else:
            a, b = self.isInBounds(i+1, j-1)
            if a and b:
                return i+1, j-1
            else:
                self.right = True
                if a:
                    return i + 1, j
                else:
                    return i, j + 1

    def isInBounds(self, i, j):
        return 0 <= i < len(self.matrix), 0 <= j < len(self.matrix[0])

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        self.matrix = matrix
        answer = []
        i, j = 0, 0
        self.right = True
        while i < len(matrix) and j < len(matrix[0]):
            answer.append(matrix[i][j])
            a, b = self.getNext(i, j)
            i = a
            j = b
        return answer
