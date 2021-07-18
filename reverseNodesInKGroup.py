# problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Runtime: 44 ms, faster than 92.86% of Python3 online submissions for Reverse Nodes in k-Group.
# Memory Usage: 15.3 MB, less than 45.77% of Python3 online submissions for Reverse Nodes in k-Group.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseInnerList(self, node, k):

        head = None
        cur = node

        while k:
            tmp = node.next
            node.next = head
            head = node
            node = tmp
            k -= 1
        return head, cur, node

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        tmp = head
        count = 0
        while tmp:
            tmp = tmp.next
            count += 1
        num_reverses = count // k
        prev, cur, node = self.reverseInnerList(head, k)
        head = prev
        num_reverses -= 1
        while num_reverses:
            prev, tmp, node = self.reverseInnerList(node, k)
            cur.next = prev
            cur = tmp
            num_reverses -= 1
        if count % k:
            cur.next = node
        return head
