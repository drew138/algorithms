# problem: https: // leetcode.com/problems/merge-two-binary-trees/
# Runtime: 92 ms, faster than 39.88 % of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 15.7 MB, less than 10.34 % of Python3 online submissions for Merge Two Binary Trees.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, t1, t2):
        if t2:
            t1.val += t2.val
        if not t1:
            return
        if t1.left:
            leftBranch = t2.left if t2 else None
            self.traverse(t1.left, leftBranch)
        elif t2 and not t1.left:
            t1.left = t2.left
        if t1.right:
            rightBranch = t2.right if t2 else None
            self.traverse(t1.right, rightBranch)
        elif t2 and not t1.right:
            t1.right = t2.right

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            t1 = TreeNode()
        self.traverse(t1, t2)
        return t1
