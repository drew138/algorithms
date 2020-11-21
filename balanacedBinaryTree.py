# problem: https://leetcode.com/problems/balanced-binary-tree/submissions/
# Runtime: 48 ms, faster than 79.17% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 18.6 MB, less than 42.89% of Python3 online submissions for Balanced Binary Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, level):
        if not node:
            return level, True
        level += 1
        left, balLeft = self.traverse(node.left, level)
        right, balRight = self.traverse(node.right, level)
        depth = max(left, right)
        return depth, (abs(left-right) <= 1 and balLeft and balRight)

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        _, isBalanced = self.traverse(root, 0)
        return isBalanced
