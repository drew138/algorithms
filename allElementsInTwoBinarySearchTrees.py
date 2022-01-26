# problem: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Runtime: 672 ms, faster than 9.42% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 17.3 MB, less than 99.70% of Python3 online submissions for All Elements in Two Binary Search Trees.

# Definition for a binary tree node.
import math
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1 = [root1] if root1 else []
        stack2 = [root2] if root2 else []
        def set_minimum(stack):
            while stack[-1].left:
                node, stack[-1].left = stack[-1].left, None
                stack.append(node)
        
        def next_node(stack):
            if not stack:
                return None
            if stack[-1].left:
                set_minimum(stack)
            node = stack.pop()
            
            val = node.val
            if node.right:
                tmp, node.right = node.right, None
                stack.append(tmp)
                set_minimum(stack)
            return val
        sol = []
        cur1 = next_node(stack1)
        cur2 = next_node(stack2)
        while cur1 != None or cur2 != None:
            tmp1 = cur1 if cur1 != None else math.inf
            tmp2 = cur2 if cur2 != None else math.inf
            if tmp1 < tmp2:
                sol.append(tmp1)
                cur1 = next_node(stack1)
            else:
                sol.append(tmp2)
                cur2 = next_node(stack2)
        return sol
                