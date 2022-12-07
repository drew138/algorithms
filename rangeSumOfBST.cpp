// problem: https://leetcode.com/problems/range-sum-of-bst/description/
// Runtime
// 325 ms
// Beats
// 20.96%
// Memory
// 64.7 MB
// Beats
// 60.79%

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
  int rangeSumBST(TreeNode *root, int low, int high) {
    if (!root)
      return 0;
    int total = 0;
    if ((root->val) >= low && (root->val) <= high)
      total += root->val;
    total += high >= (root->val) ? rangeSumBST(root->right, low, high) : 0;
    total += low <= (root->val) ? rangeSumBST(root->left, low, high) : 0;
    return total;
  }
};
