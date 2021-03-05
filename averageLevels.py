# problem: https: // leetcode.com/problems/average-of-levels-in-binary-tree/
# Runtime: 44 ms, faster than 91.19% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 16.4 MB, less than 41.77% of Python3 online submissions for Average of Levels in Binary Tree.

from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        cur = [root]
        answer = []
        nextRow = []
        while cur:

            total = 0
            for node in cur:
                total += node.val
                if node.left:
                    nextRow.append(node.left)
                if node.right:
                    nextRow.append(node.right)
            answer.append(total / len(cur))
            cur = nextRow
            nextRow = []

        return answer
