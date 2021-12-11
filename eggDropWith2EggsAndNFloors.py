# problem: https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
# Runtime: 39 ms, faster than 61.27% of Python3 online submissions for Egg Drop With 2 Eggs and N Floors.
# Memory Usage: 14.2 MB, less than 80.46% of Python3 online submissions for Egg Drop With 2 Eggs and N Floors.

class Solution:
    def twoEggDrop(self, n: int) -> int:
        sol = 0
        cur = 1
        
        while n > 0:
            sol += 1
            n -= cur
            cur += 1
        
        return sol