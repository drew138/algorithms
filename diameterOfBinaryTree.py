# problem: https: // leetcode.com/problems/diameter-of-binary-tree/
# Runtime: 40 ms, faster than 87.56 % of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16 MB, less than 79.82 % of Python3 online submissions for Diameter of Binary Tree.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, node):
        if not node:
            return 0

        right = self.traverse(node.right)
        left = self.traverse(node.left)
        self.max = max(self.max, right + left)
        return max(right + 1, left + 1)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0
        self.traverse(root)
        return self.max
