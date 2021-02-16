# problem: https://leetcode.com/problems/letter-case-permutation/
# Runtime: 56 ms, faster than 74.08% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 14.7 MB, less than 92.31% of Python3 online submissions for Letter Case Permutation.


from typing import List


class Solution:

    def traverse(self, index, s, stack):
        if index == len(s):
            self.answer.append("".join(stack))
            return
        stack.append(s[index])
        self.traverse(index+1, s, stack)
        stack.pop()
        if s[index].isalpha():
            stack.append(s[index].upper())
            self.traverse(index+1, s, stack)
            stack.pop()

    def letterCasePermutation(self, S: str) -> List[str]:
        self.answer = []
        stack = []
        S = S.lower()
        self.traverse(0, S, stack)
        return self.answer
