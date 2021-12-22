# problem: https://leetcode.com/problems/reorder-list/
# Runtime: 84 ms, faster than 94.16% of Python3 online submissions for Reorder List.
# Memory Usage: 23.1 MB, less than 99.72% of Python3 online submissions for Reorder List.


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
        

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        sol = ListNode()
        walker = head
        runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next
            if runner:
                runner = runner.next
        first = head
        second = walker.next
        walker.next = None
        second = self.reverse(second)
        cur_sol = sol
        while first or second:
            if first:
                tmp = first.next
                first.next = None
                cur_sol.next = first
                cur_sol = cur_sol.next
                first = tmp
            if second:
                tmp = second.next
                second.next = None
                cur_sol.next = second
                cur_sol = cur_sol.next
                second = tmp
        return sol.next
