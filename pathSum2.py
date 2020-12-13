# problem: https://leetcode.com/problems/path-sum-ii/
# Runtime: 40 ms, faster than 88.81% of Python3 online submissions for Path Sum II.
# Memory Usage: 15.3 MB, less than 87.29% of Python3 online submissions for Path Sum II.

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, total, stack):
        if not node:
            return None
        total += node.val
        stack.append(node.val)
        self.traverse(node.right, total, stack)
        self.traverse(node.left, total, stack)

        if not node.right and not node.left and total == self.sum:
            self.answer.append(stack.copy())
        stack.pop()
        total -= node.val

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.answer = []
        self.sum = sum
        self.traverse(root, 0, [])

        return self.answer
