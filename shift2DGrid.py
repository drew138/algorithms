# problem: https://leetcode.com/problems/shift-2d-grid/
# Runtime: 238 ms, faster than 50.14% of Python3 online submissions for Shift 2D Grid.
# Memory Usage: 14.1 MB, less than 89.14% of Python3 online submissions for Shift 2D Grid.

from typing import List

class Solution:
    
    def increase(self, i, j, m):
        if j + 1 < m:
            return i, j + 1
        return i + 1, 0    
        
    def decrease(self, i, j, m):
        if j > 0:
            return i, j -1
        return i - 1, m - 1
        
    def absPositionVal(self, i, j, m):
        return (i * m) + j    
    
    
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        
        n, m = len(grid), len(grid[0])
        k %= n * m
        
        a, b = 0, 0
        c, d = n - 1, m - 1
        while self.absPositionVal(a, b, m) < self.absPositionVal(c, d, m):
            grid[a][b], grid[c][d] = grid[c][d], grid[a][b]
            a, b = self.increase(a, b, m)
            c, d = self.decrease(c, d, m)
        
        a, b = 0, 0
        c, d = (k - 1) // m, (k - 1) % m
        x, y = self.increase(c, d, m)
        
        while self.absPositionVal(a, b, m) < self.absPositionVal(c, d, m):
            grid[a][b], grid[c][d] = grid[c][d], grid[a][b]
            a, b = self.increase(a, b, m)
            c, d = self.decrease(c, d, m)
        
        a, b = x, y
        c, d = n - 1, m - 1
        
        while self.absPositionVal(a, b, m) < self.absPositionVal(c, d, m):
            grid[a][b], grid[c][d] = grid[c][d], grid[a][b]
            a, b = self.increase(a, b, m)
            c, d = self.decrease(c, d, m)
            
        return grid
