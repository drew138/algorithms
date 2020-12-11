# problem: https: // leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Runtime: 76 ms, faster than 28.20 % of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 16.9 MB, less than 10.51 % of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, node, mid, i, j):
        if mid in self.visited or 0 > mid >= len(self.nums):
            return None
        self.visited.add(mid)

        right = (mid + j + 1) // 2
        if right < len(self.nums):
            node.right = self.traverse(
                TreeNode(self.nums[right]), right, mid, j)

        left = (mid + i) // 2
        if left >= 0:
            node.left = self.traverse(TreeNode(self.nums[left]), left, i, mid)

        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.visited = set()
        if not nums:
            return None
        self.nums = nums
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        return self.traverse(root, mid, 0, len(nums) - 1)
