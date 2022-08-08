// problem:
// https://leetcode.com/problems/longest-increasing-subsequence/submissions/
// Runtime: 8 ms, faster than 95.75% of C++ online submissions for Longest
// Increasing Subsequence. Memory Usage: 10.5 MB, less than 69.86% of C++ online
// submissions for Longest Increasing Subsequence.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int lengthOfLIS(vector<int> &nums) {
    vector<int> ans;
    ans.push_back(nums[0]);
    for (int i = 1; i < nums.size(); ++i) {
      if (nums[i] > ans[ans.size() - 1]) {
        ans.push_back(nums[i]);
      } else {
        int tmp = lower_bound(ans.begin(), ans.end(), nums[i]) - ans.begin();
        ans[tmp] = nums[i];
      }
    }
    return ans.size();
  }
};
