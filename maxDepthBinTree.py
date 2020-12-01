# problem: https: // leetcode.com/problems/maximum-depth-of-binary-tree/
# Runtime: 40 ms, faster than 70.67 % of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.1 MB, less than 23.13 % of Python3 online submissions for Maximum Depth of Binary Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, depth):
        if not node:
            return depth
        right = self.traverse(node.right, depth + 1)
        left = self.traverse(node.left, depth + 1)
        return max(right, left)

    def maxDepth(self, root: TreeNode) -> int:
        return self.traverse(root, 0)
