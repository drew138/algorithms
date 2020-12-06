# problem: https: // leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Runtime: 44 ms, faster than 87.77% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 15.4 MB, less than 12.02% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        from collections import deque
        queue = deque()
        if not root:
            return root
        cur = root
        queue.append(root)
        while queue:
            temp = []
            prev = None
            while queue:
                cur = queue.popleft()
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
                if prev != None:
                    prev.next = cur
                prev = cur
            for node in temp:
                queue.append(node)

        return root
