# problem: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Runtime: 36 ms, faster than 86.32% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 14.6 MB, less than 87.25% of Python3 online submissions for Delete Node in a Linked List.


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        while node and node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
            
            if node.next:
                node = node.next