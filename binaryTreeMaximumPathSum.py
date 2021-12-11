# problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Runtime: 173 ms, faster than 5.08% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Memory Usage: 22 MB, less than 6.93% of Python3 online submissions for Binary Tree Maximum Path Sum.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, float("-inf")
            l, cl = dfs(node.left)
            r, cr = dfs(node.right)
            return max(l + node.val, r + node.val, node.val), max(cl, cr, l + r + node.val, node.val, node.val + l, node.val + r)
        
        return dfs(root)[1]