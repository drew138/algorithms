# problem: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/submissions/
# Runtime: 164 ms, faster than 8.90% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 129.1 MB, less than 22.53% of Python3 online submissions for Maximum Difference Between Node and Ancestor.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getRange(self, node, arr):
        arr.append(node.val)
        max_left = 0
        max_right = 0
        if node.left:
            max_left = self.getRange(node.left, [*arr])
        if node.right:
            max_right = self.getRange(node.right, [*arr])
        if not (node.right or node.left):
            biggest = max(arr)
            smallest = min(arr)
            return biggest - smallest
        return max(max_right, max_left)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.getRange(root, [])
