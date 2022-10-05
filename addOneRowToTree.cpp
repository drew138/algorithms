// problem: https://leetcode.com/problems/add-one-row-to-tree/
// Runtime: 16 ms, faster than 96.79% of C++ online submissions for Add One Row
// to Tree. Memory Usage: 25 MB, less than 62.88% of C++ online submissions for
// Add One Row to Tree.

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
  void solve(TreeNode *node, int val, int depth) {
    if (!node)
      return;
    depth--;
    if (depth == 0) {

      TreeNode *left = new TreeNode(val, node->left, nullptr);
      TreeNode *right = new TreeNode{val, nullptr, node->right};

      node->left = left;
      node->right = right;
      return;
    }
    solve(node->right, val, depth);
    solve(node->left, val, depth);
  }

  TreeNode *addOneRow(TreeNode *root, int val, int depth) {
    solve(root, val, --depth);
    if (depth == 0) {
      return new TreeNode(val, root, nullptr);
    }
    return root;
  }
};
