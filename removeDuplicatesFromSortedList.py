# problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Runtime: 40 ms, faster than 79.32% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14.2 MB, less than 48.04% of Python3 online submissions for Remove Duplicates from Sorted List.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            tmp = cur.next
            while tmp and cur.val == tmp.val:
                tmp = tmp.next
            cur.next = tmp
            cur = cur.next
        return head
