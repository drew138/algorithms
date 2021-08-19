# problem: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
# Runtime: 388 ms, faster than 44.40% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# Memory Usage: 69.2 MB, less than 94.40% of Python3 online submissions for Maximum Product of Splitted Binary Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sum_tree(self, node):
        if not node:
            return 0
        return node.val + self.sum_tree(node.right) + self.sum_tree(node.left)

    def traverse(self, node):
        if not node:
            return 0
        right = self.traverse(node.right)
        left = self.traverse(node.left)
        tmp = right + left + node.val
        self.answer = max(self.answer, (self.total - tmp) * tmp)
        return tmp

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = self.sum_tree(root)
        self.answer = -float("inf")
        self.traverse(root)
        return self.answer % (10**9 + 7)
