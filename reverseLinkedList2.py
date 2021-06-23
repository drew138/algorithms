# problem: https://leetcode.com/problems/reverse-linked-list-ii/
# Runtime: 32 ms, faster than 64.41% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14.5 MB, less than 39.37% of Python3 online submissions for Reverse Linked List II.

from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, node, dif):
        cur = None
        head = node
        while dif >= 0:
            tmp = node.next
            node.next = cur
            cur = node
            node = tmp
            dif -= 1
        if node:
            head.next = node
        return cur

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dif = right - left
        cur = head
        prev = None
        tmp = left - 1
        while tmp:
            prev = cur
            cur = cur.next
            tmp -= 1
        rev = self.reverse(cur, dif)
        if prev:
            prev.next = rev
            return head
        return rev
