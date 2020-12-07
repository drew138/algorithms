# problem: https: // leetcode.com/problems/spiral-matrix-ii/
# Runtime: 36 ms, faster than 15.18 % of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 14.8 MB, less than 5.37 % of Python3 online submissions for Spiral Matrix II.

from typing import List


class Solution:
    def nextPosition(self, x, y, prev):
        right = (y == self.n - 1) or self.answer[x][y+1]
        left = (y == 0) or self.answer[x][y - 1]
        up = (x == 0) or self.answer[x - 1][y]
        down = (x == self.n - 1) or self.answer[x + 1][y]

        if prev == 'r':
            if not right:
                return x, y + 1, 'r'
        elif prev == 'd':
            if not down:
                return x + 1, y, 'd'
        elif prev == 'l':
            if not left:
                return x, y - 1, 'l'
        elif prev == 'u':
            if not up:
                return x - 1, y, 'u'

        if not right:
            return x, y + 1, 'r'
        elif not down:
            return x + 1, y, 'd'
        elif not left:
            return x, y - 1, 'l'
        elif not up:
            return x - 1, y, 'u'
        else:
            return None

    def traverse(self, x, y, r):
        self.cur += 1
        self.answer[x][y] = self.cur
        nextPosition = self.nextPosition(x, y, r)
        if nextPosition:
            self.traverse(*nextPosition)

    def generateMatrix(self, n: int) -> List[List[int]]:
        self.n = n
        self.answer = [[None for _ in range(n)] for _ in range(n)]
        self.cur = 0
        self.traverse(0, 0, 'r')
        return self.answer
