// problem: https://leetcode.com/problems/same-tree/description/
// Runtime
// 3 ms
// Beats
// 65.62%
// Memory
// 10.1 MB
// Beats
// 48.63%

#include <bits/stdc++.h>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  bool isSameTree(TreeNode *p, TreeNode *q) {
    if (!p && !q)
      return true;
    if ((!p && q) || (p && !q))
      return false;
    if (p->val != q->val)
      return false;
    bool right = isSameTree(p->right, q->right);
    bool left = isSameTree(p->left, q->left);
    return right && left;
  }
};
