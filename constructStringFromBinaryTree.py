# problem: https://leetcode.com/problems/construct-string-from-binary-tree/
# Runtime: 67 ms, faster than 73.92% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 16.4 MB, less than 30.02% of Python3 online submissions for Construct String from Binary Tree.

from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def tree2str(self, root: Optional[TreeNode]) -> str:
        arr = []

        def dfs(node):
            if not node:
                return
            arr.append(str(node.val))
            if not node.left and not node.right:
                return

            arr.append("(")
            dfs(node.left)
            arr.append(")")

            if node.right:
                arr.append("(")
                dfs(node.right)
                arr.append(")")
        dfs(root)
        return "".join(arr)
