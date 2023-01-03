// problem:
// https://leetcode.com/problems/delete-columns-to-make-sorted/description/
// Runtime
// 74 ms
// Beats
// 55.69%
// Memory
// 12.4 MB
// Beats
// 13.4%

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int minDeletionSize(vector<string> &strs) {
    vector<int> ans(strs[0].size(), 0);
    for (int i = 1; i < strs.size(); ++i) {
      for (int j = 0; j < strs[i].size(); ++j) {
        if (strs[i][j] < strs[i - 1][j])
          ans[j] = 1;
      }
    }
    return accumulate(ans.begin(), ans.end(), 0);
  }
};
