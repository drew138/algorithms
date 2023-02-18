// problem: https://leetcode.com/problems/invert-binary-tree/description/
// Runtime
// 3 ms
// Beats
// 62.83%
// Memory
// 9.8 MB
// Beats
// 46.85%

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
  TreeNode *invertTree(TreeNode *root) {
    if (!root)
      return root;
    swap(root->right, root->left);
    invertTree(root->right);
    invertTree(root->left);
    return root;
  }
};
