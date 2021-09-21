# problem: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# Runtime: 45 ms, faster than 25.26% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.
# Memory Usage: 14.2 MB, less than 88.27% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.

from typing import List


class Solution:
    def checkWinner(self, player):
        for i in range(3):
            if self.matrix[i][0] == self.matrix[i][1] == self.matrix[i][2] == player:
                return True
            if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == player:
                return True
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == player:
            return True
        if self.matrix[2][0] == self.matrix[1][1] == self.matrix[0][2] == player:
            return True
        return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        self.matrix = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        # print(moves)
        for i, (x, y) in enumerate(moves):
            player = "A" if not i % 2 else "B"
            self.matrix[x][y] = player
            # print(self.matrix)
            if self.checkWinner(player):
                return player

        return "Draw" if len(moves) == 9 else "Pending"
