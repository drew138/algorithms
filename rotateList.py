# problem: https://leetcode.com/problems/rotate-list/
# Runtime: 40 ms, faster than 49.13% of Python3 online submissions for Rotate List.
# Memory Usage: 14.2 MB, less than 61.54% of Python3 online submissions for Rotate List.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        k %= n
        k = n - k - 1
        if k == n - 1:
            return head
        cur = head
        while k:
            cur = cur.next
            k -= 1

        first = cur.next
        cur.next = None
        cur = first
        while cur and cur.next:
            cur = cur.next
        cur.next = head
        
        return first