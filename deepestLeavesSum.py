# problem: https: // leetcode.com/problems/deepest-leaves-sum/
# Runtime: 92 ms, faster than 71.10% of Python3 online submissions for Deepest Leaves Sum.
# Memory Usage: 17.5 MB, less than 97.51% of Python3 online submissions for Deepest Leaves Sum.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        from collections import deque
        queue = deque([root])
        total = None
        while queue:
            tmp = deque()
            cur = 0
            while queue:
                element = queue.popleft()
                cur += element.val
                if element.left:
                    tmp.append(element.left)
                if element.right:
                    tmp.append(element.right)
            total = cur
            queue = tmp
        return total
