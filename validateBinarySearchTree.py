# problme: https: // leetcode.com/problems/validate-binary-search-tree/submissions/
# Runtime: 44 ms, faster than 65.81 % of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.3 MB, less than 72.28 % of Python3 online submissions for Validate Binary Search Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, low, high):
        if not node:
            return
        if node.left and self.isValid:
            self.isValid = node.val > node.left.val > low
            self.isValid and self.traverse(node.left, low, node.val)
        if node.right and self.isValid:
            self.isValid = node.val < node.right.val < high
            self.isValid and self.traverse(node.right, node.val, high)

    def isValidBST(self, root: TreeNode) -> bool:
        self.isValid = True
        self.traverse(root, -float("inf"), float("inf"))
        return self.isValid
