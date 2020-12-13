# problem: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Runtime: 32 ms, faster than 82.62% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
# Memory Usage: 14.4 MB, less than 46.20% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, depth):
        if not node:
            return depth
        self.depth = max(self.depth, depth)
        right = self.traverse(node.right, depth + 1)
        left = self.traverse(node.left, depth + 1)
        if right == left and right > self.depth:
            self.subtree = node
        return max(right, left)

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.subtree = root
        self.depth = 0
        self.traverse(root, 0)
        return self.subtree
