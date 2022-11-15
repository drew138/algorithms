// problem: https://leetcode.com/problems/count-complete-tree-nodes/
// Runtime: 64 ms, faster than 55.74% of C++ online submissions for Count
// Complete Tree Nodes. Memory Usage: 31 MB, less than 20.93% of C++ online
// submissions for Count Complete Tree Nodes.

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
  int countNodes(TreeNode *root) {
    int l_depth = 0;
    int r_depth = 0;
    TreeNode *l = root;
    TreeNode *r = root;
    while (l) {
      l_depth++;
      l = l->left;
    }
    while (r) {
      r_depth++;
      r = r->right;
    }

    if (l_depth == r_depth)
      return pow(2, l_depth) - 1;
    return 1 + countNodes(root->left) + countNodes(root->right);
  }
};
