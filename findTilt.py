
# problem: https://leetcode.com/problems/binary-tree-tilt/submissions/
# Runtime: 56 ms, faster than 72.43% of Python3 online submissions for Binary Tree Tilt.
# Memory Usage: 15.7 MB, less than 96.11% of Python3 online submissions for Binary Tree Tilt.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def tilt(self, node):
        if not node:
            return 0
        left = self.tilt(node.left)
        right = self.tilt(node.right)
        self.result += abs(left - right)
        return left + right + node.val

    def findTilt(self, root: TreeNode) -> int:
        self.result = 0
        self.tilt(root)
        return self.result
