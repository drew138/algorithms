# problem: https://leetcode.com/problems/search-in-a-binary-search-tree/
# Runtime: 77 ms, faster than 86.80% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16.5 MB, less than 28.83% of Python3 online submissions for Search in a Binary Search Tree.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or val == root.val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)