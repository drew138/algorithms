# problem: https://leetcode.com/problems/path-sum-iii/
# Runtime: 49 ms, faster than 76.08% of Python3 online submissions for Path Sum III.
# Memory Usage: 15.8 MB, less than 29.10% of Python3 online submissions for Path Sum III.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        from collections import defaultdict
        counter = defaultdict(int)
        counter[0] = 1

        def dfs(root, cur):
            if not root:
                return 0
            tmp = cur + root.val
            s = counter[tmp - target]
            counter[tmp] += 1

            l = dfs(root.left, tmp)
            r = dfs(root.right, tmp)

            counter[tmp] -= 1
            return l + r + s
        return dfs(root, 0)
