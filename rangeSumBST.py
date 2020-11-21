# problem:https://leetcode.com/problems/range-sum-of-bst/
# Runtime: 208 ms, faster than 78.22% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22.2 MB, less than 32.15% of Python3 online submissions for Range Sum of BST.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _isInBounds(self, node):
        return self.low <= node.val <= self.high

    def _isHigher(self, node):
        return node.val > self.high

    def _isLower(self, node):
        return node.val < self.low

    def _traverse(self, node):
        if not node:
            return
        if self._isInBounds(node):
            self.total += node.val
        if not self._isLower(node):
            self._traverse(node.left)
        if not self._isHigher(node):
            self._traverse(node.right)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.total = 0
        if not root:
            return self.total
        self._traverse(root)
        return self.total
