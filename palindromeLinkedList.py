# problem: https://leetcode.com/problems/palindrome-linked-list/
# Runtime: 736 ms, faster than 45.39% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 39.1 MB, less than 48.52% of Python3 online submissions for Palindrome Linked List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, node):
        cur = None
        while node:
            tmp = node.next
            node.next = cur
            cur = node
            node = tmp
        return cur

    def isPalindrome(self, head: ListNode) -> bool:
        walker = head
        runner = head
        while runner:
            walker = walker.next
            runner = runner.next
            if runner:
                runner = runner.next
        rev = self.reverse(walker)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
