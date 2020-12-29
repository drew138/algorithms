# problem: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# Runtime: 580 ms, faster than 24.21% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
# Memory Usage: 49.2 MB, less than 88.95% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, node, stack):
        if not node:
            return
        stack.append(node.val)
        if not node.left and not node.right:
            for num in stack:
                self.counter[num - 1] += 1
            numOdds = 0
            for num in self.counter:
                if num % 2 == 1:
                    numOdds += 1
            if numOdds <= 1:
                self.answer += 1
            for i in range(len(self.counter)):
                self.counter[i] = 0
            stack.pop()
            return

        self.traverse(node.right, stack)
        self.traverse(node.left, stack)
        stack.pop()

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.answer = 0
        self.counter = [0] * 9
        self.traverse(root, [])
        return self.answer
