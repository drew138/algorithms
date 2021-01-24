# problem: https: // leetcode.com/problems/merge-k-sorted-lists/submissions/
# Runtime: 5492 ms, faster than 5.49 % of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.7 MB, less than 93.87 % of Python3 online submissions for Merge k Sorted Lists.


from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        head = lists.pop()
        while lists:
            cur = head
            tmp = lists.pop()
            prev = cur
            while cur or tmp:
                if (cur and not tmp) or (cur and cur.val < tmp.val):
                    prev = cur
                    cur = cur.next
                else:
                    if prev is cur:
                        next = tmp.next
                        tmp.next = cur
                        prev = tmp
                        head = prev
                        tmp = next
                    else:
                        prev.next = tmp
                        next = tmp.next
                        prev = tmp
                        tmp.next = cur
                        tmp = next
        return head
