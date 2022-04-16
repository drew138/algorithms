# problem: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# Runtime: 668 ms, faster than 94.05% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
# Memory Usage: 138.5 MB, less than 28.95% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def traverse(node, val, path, direction = ''):
            if not node: return False
            
            found = node.val == val
            found = found or traverse(node.left, val, path, 'L')
            found = found or traverse(node.right, val, path, 'R')
            if found:
                path.append(direction)
            
            return found
        start_path, dest_path = [], []
        traverse(root, startValue, start_path)
        traverse(root, destValue, dest_path)
        start_path.reverse()
        dest_path.reverse()
        i = 0
        len_start = len(start_path)
        len_dest = len(dest_path)
        while i < len_start and i < len_dest and start_path[i] == dest_path[i]:
            i += 1
        return "U" * (len_start - i) + "".join(dest_path[i:])
        