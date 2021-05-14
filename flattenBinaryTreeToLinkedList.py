# problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Runtime: 36 ms, faster than 74.13% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.3 MB, less than 12.74% of Python3 online submissions for Flatten Binary Tree to Linked List.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node):
        if not node:
            return node, None
        elif not node.left and not node.right:
            return node, node
        l, lt = self.traverse(node.left)
        r, rt = self.traverse(node.right)
        if l and lt:
            node.right = l
            lt.right = r
        else:
            node.right = r
        if not rt:
            rt = lt
        node.left = None
        return node, rt

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
