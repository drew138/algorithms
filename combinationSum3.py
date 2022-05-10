# problem: https://leetcode.com/problems/combination-sum-iii/
# Runtime: 59 ms, faster than 17.68% of Python3 online submissions for Combination Sum III.
# Memory Usage: 13.9 MB, less than 79.39% of Python3 online submissions for Combination Sum III.


from typing import List


class Solution:
    
    def get_combinations(self, k, n, start, stack, answer):
        if not k and not n:
            answer.append(stack.copy())
            return
            
        for i in range(start, 10):
            stack.append(i)
            self.get_combinations(k - 1, n - i, i + 1, stack, answer)
            stack.pop()
        
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        self.get_combinations(k, n, 1, [], answer)
        return answer
