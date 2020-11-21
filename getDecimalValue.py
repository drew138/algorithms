# problem: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/
# Runtime: 32 ms, faster than 53.95% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        :type head: ListNode
        :rtype: int
        """
        answer = 0
        while head:
            answer <<= 1
            answer += head.val
            head = head.next
        return answer
