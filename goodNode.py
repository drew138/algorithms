# problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Runtime: 244 ms, faster than 70.82% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 33.6 MB, less than 6.52% of Python3 online submissions for Count Good Nodes in Binary Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, parentVal):
        if not node:
            return
        else:
            if node.val >= parentVal:
                self.numPaths += 1
        if node.left:
            self.traverse(node.left, max(parentVal, node.val))
        if node.right:
            self.traverse(node.right, max(parentVal, node.val))

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.numPaths = 0
        self.traverse(root, root.val)
        return self.numPaths
