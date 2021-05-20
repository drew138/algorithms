# problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Runtime: 44 ms, faster than 6.68% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.7 MB, less than 44.20% of Python3 online submissions for Binary Tree Level Order Traversal.

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        answer = []
        if not root:
            return answer
        queue = deque()

        queue.append(root)
        while queue:
            tmp = deque()
            l = []
            while queue:
                n = queue.popleft()
                l.append(n.val)
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            answer.append(l)
            queue = tmp
        return answer
