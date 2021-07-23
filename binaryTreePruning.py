# problem: https://leetcode.com/problems/binary-tree-pruning/
# Runtime: 28 ms, faster than 86.42% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 14.3 MB, less than 22.41% of Python3 online submissions for Binary Tree Pruning.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node):
        if not node:
            return False
        l = self.traverse(node.left)
        r = self.traverse(node.right)
        if not l:
            node.left = None
        if not r:
            node.right = None
        return l or r or node.val == 1

    def pruneTree(self, root: TreeNode) -> TreeNode:
        r = self.traverse(root)
        if not r:
            return None
        return root
