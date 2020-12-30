# problem: https://leetcode.com/problems/game-of-life/submissions/
# Runtime: 32 ms, faster than 75.07% of Python3 online submissions for Game of Life.
# Memory Usage: 14.5 MB, less than 8.28% of Python3 online submissions for Game of Life.

from typing import List


class Solution:
    def getNeighbors(self, i, j):
        neighbours = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]
        zeroes = 0
        ones = 0
        for n in neighbours:
            if 0 <= i + n[0] < len(self.board) and 0 <= j + n[1] < len(self.board[i]):
                num = self.board[i+n[0]][j+n[1]]
                if num == 1 or num == -1:
                    ones += 1
                elif num == 0 or num == -2:
                    zeroes += 1
        if self.board[i][j] == 1:
            if ones < 2:
                self.board[i][j] = -1
            elif ones > 3:
                self.board[i][j] = -1
        else:
            if ones == 3:
                self.board[i][j] = -2

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.getNeighbors(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.board[i][j] == -1:
                    self.board[i][j] = 0
                elif self.board[i][j] == -2:
                    self.board[i][j] = 1
