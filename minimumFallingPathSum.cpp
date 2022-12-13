// problem: https://leetcode.com/problems/minimum-falling-path-sum/description/
// Runtime
// 8 ms
// Beats
// 99.50%
// Memory
// 9.7 MB
// Beats
// 99.78%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int minFallingPathSum(vector<vector<int>> &matrix) {
    int imax = INT_MAX;
    for (int i = 1; i < matrix.size(); ++i) {
      for (int j = 0; j < matrix[i].size(); ++j) {
        int left = j > 0 ? matrix[i - 1][j - 1] : imax;
        int mid = matrix[i - 1][j];
        int right = j + 1 < matrix[0].size() ? matrix[i - 1][j + 1] : imax;
        matrix[i][j] += min(left, min(mid, right));
      }
    }
    int ans = imax;
    for (int i = 0; i < matrix[matrix.size() - 1].size(); ++i) {
      ans = min(ans, matrix[matrix.size() - 1][i]);
    }
    return ans;
  }
};
