# problem: https://leetcode.com/problems/invert-binary-tree/submissions/
# Runtime: 44 ms, faster than 6.02% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 14.3 MB, less than 44.67% of Python3 online submissions for Invert Binary Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root
