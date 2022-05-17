// problem: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
// Runtime: 593 ms, faster than 71.97% of C++ online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
// Memory Usage: 166 MB, less than 5.16% of C++ online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.

#include <bits/stdc++.h>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        queue<pair<TreeNode*, TreeNode*>> q;
        q.push({ original, cloned });
        while (!q.empty()) {
            pair<TreeNode*, TreeNode*> cur = q.front(); q.pop();
            TreeNode* first = cur.first;
            TreeNode* second = cur.second;
            if (first == target) return second;
            if (first -> right) q.push({ first -> right, second -> right});
            if (first -> left) q.push({ first -> left, second -> left });
        }
        return NULL;
    }
};
