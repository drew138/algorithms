# problem: https://leetcode.com/problems/binary-tree-right-side-view/
# Runtime: 32 ms, faster than 71.24% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 14.1 MB, less than 81.62% of Python3 online submissions for Binary Tree Right Side View.

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        from collections import deque
        queue = deque()
        queue.append(root)
        answer = []
        while queue:
            tmp = deque()
            n = queue.popleft()
            answer.append(n.val)
            if n.right:
                tmp.append(n.right)
            if n.left:
                tmp.append(n.left)
            while queue:
                n = queue.popleft()
                if n.right:
                    tmp.append(n.right)
                if n.left:
                    tmp.append(n.left)
            queue = tmp
        return answer
