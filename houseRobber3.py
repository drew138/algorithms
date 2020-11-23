# problem: https://leetcode.com/problems/house-robber-iii/submissions/
# Runtime: 44 ms, faster than 87.60% of Python3 online submissions for House Robber III.
# Memory Usage: 16 MB, less than 42.04% of Python3 online submissions for House Robber III.

# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, node):
        if node == None:
            return [0, 0]

        left = self.traverse(node.left)
        right = self.traverse(node.right)
        res = [0, 0]

        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = node.val + left[0] + right[0]
        return res

    def rob(self, root: TreeNode) -> int:
        return max(self.traverse(root))
