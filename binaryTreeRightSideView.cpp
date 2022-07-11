#include <bits/stdc++.h>


using namespace std;



// Definition for a binary tree node.
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
    vector<int> rightSideView(TreeNode* root) {
        queue<TreeNode*> q;
        if (root) q.push(root);
        vector<int> ans;
        while (q.size()) {
            queue<TreeNode*> tmp;
            ans.push_back(q.front() -> val);
            while (q.size()){
                TreeNode* cur = q.front();
                q.pop();
                if (cur -> right) tmp.push(cur -> right);
                if (cur -> left) tmp.push(cur -> left);
            }
            q = tmp;
            
        }
        return ans;
    }
};