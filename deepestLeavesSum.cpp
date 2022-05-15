// problem: https://leetcode.com/problems/deepest-leaves-sum/
// Runtime: 131 ms, faster than 48.98% of C++ online submissions for Deepest Leaves Sum.
// Memory Usage: 62.3 MB, less than 12.68% of C++ online submissions for Deepest Leaves Sum.

#include <bits/stdc++.h>


using namespace std;

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        
        queue<TreeNode*> q;
        int sol = 0;
        q.push(root);
        while (!q.empty()) {
            sol = 0;
            queue<TreeNode*> tmp;
            while (!q.empty()) {
                TreeNode* cur = q.front();
                q.pop();
                sol += cur -> val;
                if (cur -> left) tmp.push(cur -> left);
                if (cur -> right) tmp.push(cur -> right);
            }
            q = tmp;
        }
        return sol;
    }
};
