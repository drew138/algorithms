# problem: https://leetcode.com/problems/robot-bounded-in-circle/
# Runtime: 28 ms, faster than 86.38% of Python3 online submissions for Robot Bounded In Circle.
# Memory Usage: 14.3 MB, less than 50.00% of Python3 online submissions for Robot Bounded In Circle.

class Solution:
    
    def setOrientation(self, cur, val):
        if 0 < cur and val == 'L':
            cur -= 1
        elif cur == 0 and val == 'L':
            cur = 3
        elif cur == 3 and val == 'R':
            cur = 0
        elif cur < 3 and val == 'R':
            cur += 1
        return cur
    
    def increasePosition(self, orientation, x, y):
        if orientation == 0:
            y += 1
        elif orientation == 1:
            x += 1
        elif orientation == 2:
            y -= 1
        else:
            x -= 1
        return x, y
            
    def isRobotBounded(self, instructions: str) -> bool:
        
        orientation = 0
        x, y = 0, 0
        for instruction in instructions:
            if instruction == 'G':
                x, y = self.increasePosition(orientation, x, y)
            else:
                orientation = self.setOrientation(orientation, instruction)
                
        return (x, y) == (0, 0) or orientation != 0