# problem: https: // leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Runtime: 76 ms, faster than 71.07 % of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18.2 MB, less than 22.41 % of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def traverse(self, node):

        if node.val > self.p.val and node.val > self.q.val:
            self.traverse(node.left)
        elif node.val < self.p.val and node.val < self.q.val:
            self.traverse(node.right)
        else:
            self.answer = node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.answer = None
        self.traverse(root)
        return self.answer
