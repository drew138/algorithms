# problem: https://leetcode.com/problems/linked-list-cycle-ii/
# Runtime: 103 ms, faster than 6.91% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.3 MB, less than 56.58% of Python3 online submissions for Linked List Cycle II.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        walker = head
       
        while runner:
            
            walker = walker.next
            runner = runner.next
            if not runner or not runner.next:
                return None
            runner = runner.next
            if runner is walker:
                break

        sol = head
        while sol is not walker:
            sol = sol.next
            walker = walker.next
        return sol
