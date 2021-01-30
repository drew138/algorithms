# problem: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Runtime: 32 ms, faster than 80.48% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
# Memory Usage: 14.6 MB, less than 36.16% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, x, y):
        if not node:
            return
        self.min = min(self.min, x)
        self.max = max(self.max, x)
        self.m[x].append((y, node.val))
        self.traverse(node.right, x + 1, y + 1)
        self.traverse(node.left, x - 1, y + 1)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        self.m = defaultdict(list)
        self.min = 0
        self.max = 0
        self.traverse(root, 0, 0)
        return [[m[1] for m in sorted(self.m[n], key=lambda x: (x[0], x[1]))] for n in range(self.min, self.max + 1)]
