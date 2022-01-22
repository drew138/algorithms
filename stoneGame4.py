# problem: https://leetcode.com/problems/stone-game-iv/
# Runtime: 4976 ms, faster than 13.77% of Python3 online submissions for Stone Game IV.
# Memory Usage: 127.2 MB, less than 23.95% of Python3 online submissions for Stone Game IV.


class Solution:
    dp = {}
    
    def generate_squares(self, n):
        i = 1
        while i * i <= n:
            yield i * i
            i += 1
    
    def solve(self, n, player):
        if (n, player) in self.dp:
            return self.dp[(n, player)]
        if n == 0:
            return player != 'a'
        
        other = 'a' if player == 'b' else 'b'
        val = player == 'b'
        for i in self.generate_squares(n):
            res = self.solve(n - i, other)
            if other == 'b':
                val = val or res
                if val == True:
                    break
            else:
                val = val and res
                if not val:
                    break
        self.dp[(n, player)] = val

        return val
        
    
    def winnerSquareGame(self, n: int) -> bool:
        res = self.solve(n, 'a')

        return res