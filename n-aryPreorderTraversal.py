# problem: https: // leetcode.com/problems/n-ary-tree-preorder-traversal/
# Runtime: 48 ms, faster than 79.68% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16 MB, less than 20.99% of Python3 online submissions for N-ary Tree Preorder Traversal.

from typing import List

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        from collections import deque
        stack = deque()
        stack.append(root)
        answer = []
        if not root:
            return answer
        while stack:
            node = stack.pop()
            answer.append(node.val)
            for children in reversed(node.children):
                stack.append(children)
        return answer
