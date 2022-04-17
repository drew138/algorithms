# problem: https://leetcode.com/problems/permutations/
# Runtime: 43 ms, faster than 83.72% of Python3 online submissions for Permutations.
# Memory Usage: 14.2 MB, less than 23.61% of Python3 online submissions for Permutations.

from collections import Counter
from typing import List

class Solution:
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        stack = []
        answer = []
        n = len(nums)
        def traverse(stack):
            if len(stack) == n:
                answer.append(stack.copy())
                return
                
            for key in counter.keys():
                if counter[key]:
                    counter[key] -=1
                    stack.append(key)
                    traverse(stack)
                    stack.pop()
                    counter[key] += 1
        traverse(stack)
        return answer