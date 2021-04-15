# probleml: https: // leetcode.com/problems/partition-list/
# Runtime: 28 ms, faster than 94.16 % of Python3 online submissions for Partition List.
# Memory Usage: 14.4 MB, less than 31.00 % of Python3 online submissions for Partition List.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        listOne = ListNode()
        startOne = listOne
        listTwo = ListNode()
        startTwo = listTwo

        while head:
            if head.val < x:
                listOne.next = head
                head = head.next
                listOne = listOne.next
                listOne.next = None
            else:
                listTwo.next = head
                head = head.next
                listTwo = listTwo.next
                listTwo.next = None
        if startOne.next:
            listOne.next = startTwo.next
            return startOne.next
        return startTwo.next
