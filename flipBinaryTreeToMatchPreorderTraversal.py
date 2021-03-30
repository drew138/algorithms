# problem: https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
# Runtime: 36 ms, faster than 61.02% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
# Memory Usage: 14.2 MB, less than 68.36% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.

from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node):
        if not node:
            return True
        if node.val != self.voyage[self.i]:
            return False
        self.i += 1
        if node.left and node.left.val != self.voyage[self.i]:
            self.l.append(node.val)
            return self.traverse(node.right) and self.traverse(node.left)
        else:
            return self.traverse(node.left) and self.traverse(node.right)

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.l = []
        self.voyage = voyage
        self.i = 0
        var = self.traverse(root)
        return self.l if var else [-1]
