#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    vector<int> merge(vector<int> &a, vector<int> &b) {
        vector<int> ret;
        int i = 0, j = 0;
        while (i < a.size() || j < b.size()) {
            int first = i < a.size() ? a[i] : INT_MAX, second = j < b.size() ? b[j]: INT_MAX;
            if (first < second) {
                ret.push_back(first);
                i++;
            } else {
                ret.push_back(second);
                j++;
            }
        }
        return ret;
    }
    
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int> prev = matrix[0];
        
        while (matrix.size() > 1) {
            vector<vector<int>> tmp;
            vector<int> cur;
            for (int i = 0; i < matrix.size(); i += 2) {
                if (i + 1 < matrix.size()) {
                    cur = merge(matrix[i], matrix[i+ 1]);
                } else {
                    cur = matrix[i];
                }
                tmp.push_back(cur);
            }
            matrix = tmp;
        }
        return matrix[0][k - 1];
    }
};
