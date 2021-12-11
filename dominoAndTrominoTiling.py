# problem: https://leetcode.com/problems/domino-and-tromino-tiling/
# Runtime: 64 ms, faster than 15.13% of Python3 online submissions for Domino and Tromino Tiling.
# Memory Usage: 16.9 MB, less than 8.46% of Python3 online submissions for Domino and Tromino Tiling.

class Solution:
    def numTilings(self, n: int) -> int:
        cache = {}
        def backtrack(first, second):
            if (first, second) in cache:
                return cache[(first, second)]
            
            if first > n or second > n:
                return 0
            
            if first == second == n:
                return 1
            
            total = 0
            if first == second:
                total += backtrack(first + 1, second + 1)
                total += backtrack(first + 2, second + 2)
                total += backtrack(first + 1, second + 2)
                total += backtrack(first + 2, second + 1)
            elif first > second:
                total += backtrack(first + 1, second + 2)
                total += backtrack(first, second + 2)
            else:
                total += backtrack(first + 2, second + 1)
                total += backtrack(first + 2, second)
        
            cache[(first, second)] = total
            return total % (10 **9 + 7)
        
        return backtrack(0, 0)