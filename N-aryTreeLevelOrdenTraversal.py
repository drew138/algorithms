# problem: https: // leetcode.com/problems/n-ary-tree-level-order-traversal/
# Runtime: 98 ms, faster than 5.44 % of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 15.9 MB, less than 97.61 % of Python3 online submissions for N-ary Tree Level Order Traversal.

from typing import List

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        queue = []
        if not root:
            return queue
        queue.append(root)
        answer = []
        while queue:
            tmp = []
            answer.append([n.val for n in queue])
            for n in queue:
                tmp += [child for child in n.children]
            queue = tmp
        return answer
