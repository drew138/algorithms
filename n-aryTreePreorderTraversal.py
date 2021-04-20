# problem: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Runtime: 48 ms, faster than 80.92% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.1 MB, less than 20.27% of Python3 online submissions for N-ary Tree Preorder Traversal.

from typing import List

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def traverse(self, node):
        if not node:
            return
        self.answer.append(node.val)
        for child in node.children:
            self.traverse(child)

    def preorder(self, root: 'Node') -> List[int]:
        self.answer = []
        self.traverse(root)
        return self.answer
