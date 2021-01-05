# problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Runtime: 40 ms, faster than 71.84% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 14.4 MB, less than 22.81% of Python3 online submissions for Remove Duplicates from Sorted List II.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        prev = None
        cur = head
        head = None
        while cur:
            tmp = cur.next
            unique = cur != tmp
            while tmp and tmp.val == cur.val:
                unique = False
                tmp = tmp.next
            if unique and not head:
                head = cur
            if unique:
                if prev:
                    prev.next = cur
                prev = cur
            elif not tmp and prev:
                prev.next = None
            cur = tmp
        return head
