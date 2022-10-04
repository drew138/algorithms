// problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Runtime: 10 ms, faster than 33.90% of C++ online submissions for Remove Nth
// Node From End of List. Memory Usage: 10.7 MB, less than 75.00% of C++ online
// submissions for Remove Nth Node From End of List.

#include <bits/stdc++.h>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    ListNode *walker = head;
    ListNode *runner = head;
    while (n--)
      runner = runner->next;
    if (!runner)
      return head->next;
    while (runner && runner->next) {
      walker = walker->next;
      runner = runner->next;
    }
    ListNode *next = walker->next;
    walker->next = next != nullptr ? next->next : nullptr;
    return head;
  }
};
