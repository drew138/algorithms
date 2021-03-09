# problem: https://leetcode.com/problems/add-one-row-to-tree/
# Runtime: 48 ms, faster than 93.90% of Python3 online submissions for Add One Row to Tree.
# Memory Usage: 16.9 MB, less than 48.01% of Python3 online submissions for Add One Row to Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, d, v):
        if not node:
            return
        if not d-1:
            tmp = node.left
            node.left = TreeNode(val=v, left=tmp)
            tmp = node.right
            node.right = TreeNode(val=v, right=tmp)
            return
        self.traverse(node.left, d-1, v)
        self.traverse(node.right, d-1, v)

    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not d-1:
            return TreeNode(val=v, left=root)
        self.traverse(root, d-1, v)
        return root
