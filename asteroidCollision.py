# problem: https://leetcode.com/problems/asteroid-collision/
# Runtime: 104 ms, faster than 82.99% of Python3 online submissions for Asteroid Collision.
# Memory Usage: 15.2 MB, less than 83.52% of Python3 online submissions for Asteroid Collision.

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sol = []  
        stack = []
        for asteroid in asteroids:
            if asteroid >= 0:
                stack.append(asteroid)
            else:
                is_equal = False
                while stack and abs(stack[-1]) <= abs(asteroid):
                    if abs(stack[-1]) == abs(asteroid):
                        is_equal = True
                        stack.pop()
                        break
                    stack.pop()
                if not (stack or is_equal):
                    sol.append(asteroid)
        sol += stack
        return sol
