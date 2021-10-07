# problem: https://leetcode.com/problems/word-search/
# Runtime: 7976 ms, faster than 22.61% of Python3 online submissions for Word Search.
# Memory Usage: 14.2 MB, less than 69.24% of Python3 online submissions for Word Search.

from typing import List


class Solution:
    dirs = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    def dfs(self, i, j, index=1):

        if index == len(self.word):
            self.found = True

        for x, y in self.dirs:
            if self.found:
                break
            if 0 <= x + i < self.n and 0 <= y + j < self.m:
                character = self.board[x+i][y+j]
                coordinate = (x+i, y+j)
                if (not coordinate in self.visited) and character == self.word[index]:
                    self.visited.add(coordinate)
                    self.dfs(x + i, y + j, index + 1)
                    self.visited.remove(coordinate)

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n, self.m = len(board), len(board[0])
        self.board = board
        self.word = word
        self.found = False
        for i in range(self.n):
            for j in range(self.m):
                if self.word[0] == board[i][j]:

                    self.visited = set([(i, j)])
                    self.dfs(i, j)
                    if self.found:
                        return True
        return False
