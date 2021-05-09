# problem: https://leetcode.com/problems/odd-even-linked-list/
# Runtime: 64 ms, faster than 8.94% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 16.4 MB, less than 57.90% of Python3 online submissions for Odd Even Linked List.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        evenList = ListNode()
        oddList = ListNode()
        tmpEven = evenList
        tmpOdd = oddList
        i = 1
        while head:
            tmp = head
            head = head.next
            if i % 2 == 0:
                tmpEven.next = tmp
                tmpEven = tmpEven.next
                tmpEven.next = None
            else:
                tmpOdd.next = tmp
                tmpOdd = tmpOdd.next
                tmpOdd.next = None
            i += 1
        tmpOdd.next = evenList.next
        return oddList.next
