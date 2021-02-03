# problem : https://leetcode.com/problems/trim-a-binary-search-tree/
# Runtime: 44 ms, faster than 92.77% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 18.2 MB, less than 78.91% of Python3 online submissions for Trim a Binary Search Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return root
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
