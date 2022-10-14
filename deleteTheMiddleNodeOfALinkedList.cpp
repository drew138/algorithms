// problem:
// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
// Runtime: 1030 ms, faster than 98.52% of C++ online submissions for Delete the
// Middle Node of a Linked List. Memory Usage: 294.9 MB, less than 20.46% of C++
// online submissions for Delete the Middle Node of a Linked List.

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
  ListNode *deleteMiddle(ListNode *head) {
    if (!head->next)
      return nullptr;
    ListNode *walker = head;
    ListNode *runner = head;
    while (runner && runner->next) {
      walker = walker->next;
      runner = runner->next;
      if (runner)
        runner = runner->next;
    }
    if (head->next == walker)
      head->next = head->next ? head->next->next : nullptr;
    else
      *walker = *walker->next;

    return head;
  }
};
