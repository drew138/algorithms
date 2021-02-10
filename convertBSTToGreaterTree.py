# problem: https://leetcode.com/problems/convert-bst-to-greater-tree/
# Runtime: 84 ms, faster than 58.69% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 16.8 MB, less than 50.21% of Python3 online submissions for Convert BST to Greater Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, node):
        if not node:
            return
        self.traverse(node.right)
        tmp = node.val
        node.val += self.cur
        self. cur += tmp
        self.traverse(node.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.cur = 0
        self.traverse(root)
        return root
