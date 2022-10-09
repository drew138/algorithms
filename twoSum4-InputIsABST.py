# problem: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Runtime: 221 ms, faster than 14.97% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 18.3 MB, less than 40.47% of Python3 online submissions for Two Sum IV - Input is a BST.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        m = set()
        def traverse(node):
            if not node: return False
            tmp = ((k - node.val) in m)
            m.add(node.val)
            return tmp or traverse(node.right) or traverse(node.left)

        return traverse(root)
