# problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Runtime: 68 ms, faster than 85.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 25.9 MB, less than 43.05% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def traverse(self, node, p, q):

        if not node:
            return None, False, False
        l, lp, lq = self.traverse(node.left, p, q)
        if l:
            return (l, lp, lq)
        r, rp, rq = self.traverse(node.right, p, q)
        if r:
            return (r, rp, rq)
        if node == p:
            return (node, True, True) if (lq or rq) else (None, True, False)
        if node == q:
            return (node, True, True) if (lp or rp) else (None, False, True)
        return (node, True, True) if ((lp or rp) and (lq or rq)) else (None, (lp or rp), (lq or rq))

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a, b, c = self.traverse(root, p, q)
        return a
