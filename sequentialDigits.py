# problem: https://leetcode.com/problems/sequential-digits/
# Runtime: 49 ms, faster than 20.24% of Python3 online submissions for Sequential Digits.
# Memory Usage: 14.2 MB, less than 80.16% of Python3 online submissions for Sequential Digits.

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        sol = []
        def generate_numbers(arr, low, high, start):
            if low <= start <= high:
                arr.append(start)
            for i in range(start + 1, 10):
                start *= 10
                start += i
                if low <= start <= high:
                    arr.append(start)
            
        
        for i in range(1, 10):
            generate_numbers(sol, low, high, i)
        sol.sort()
        return sol