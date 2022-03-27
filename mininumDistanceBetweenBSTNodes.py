# problem: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Runtime: 35 ms, faster than 84.98% of Python3 online submissions for Minimum Distance Between BST Nodes.
# Memory Usage: 13.9 MB, less than 83.57% of Python3 online submissions for Minimum Distance Between BST Nodes.


import math

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.prev = -math.inf
        self.answer = math.inf
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:


        if not root:
            return self.answer

        left_solution = self.minDiffInBST(root.left) 
        
        self.answer = min(self.answer, root.val - self.prev)
        self.prev = root.val
        right_solution = self.minDiffInBST(root.right)

        return self.answer
