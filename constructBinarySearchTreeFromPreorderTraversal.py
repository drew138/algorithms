# problem: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Runtime: 36 ms, faster than 81.10% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 14.4 MB, less than 44.72% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.


from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, parent_value):

        if self.index == len(self.preorder):
            return None
        val = self.preorder[self.index]
        self.index += 1
        inbounds = self.index < len(self.preorder)
        left = self.traverse(
            val) if inbounds and self.preorder[self.index] < val else None
        inbounds = self.index < len(self.preorder)
        right = self.traverse(max(val, parent_value)) if inbounds and (
            val < self.preorder[self.index] < parent_value) else None
        return TreeNode(val, left, right)

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        self.preorder = preorder
        return self.traverse(float("inf"))
