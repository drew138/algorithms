// problem: https://leetcode.com/problems/path-sum/
// Runtime: 23 ms, faster than 35.50% of C++ online submissions for Path Sum.
// Memory Usage: 21.1 MB, less than 92.08% of C++ online submissions for Path
// Sum.

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
  bool solve(TreeNode *root, int targetSum) {
    if (!root)
      return false;
    targetSum -= root->val;
    if (!root->right && !root->left)
      return targetSum == 0;
    return solve(root->right, targetSum) || solve(root->left, targetSum);
  }
  bool hasPathSum(TreeNode *root, int targetSum) {
    if (!root)
      return false;
    return solve(root, targetSum);
  }
};
