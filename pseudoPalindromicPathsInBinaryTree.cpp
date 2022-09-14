
// problem:
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
// Runtime: 702 ms, faster than 33.67% of C++ online submissions for
// Pseudo-Palindromic Paths in a Binary Tree. Memory Usage: 178.6 MB, less
// than 97.90% of C++ online submissions for Pseudo-Palindromic Paths in a
// Binary Tree.

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
  int dfs(TreeNode *root, int num) {
    if (!root)
      return 0;
    num ^= 1 << (root->val);
    if (!root->right && !root->left)
      return ((num - 1) & num) == 0;
    return dfs(root->right, num) + dfs(root->left, num);
  }

  int pseudoPalindromicPaths(TreeNode *root) { return dfs(root, 0); }
};
