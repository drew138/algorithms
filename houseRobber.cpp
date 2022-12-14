// problem: https://leetcode.com/problems/house-robber/description/
// Runtime
// 5 ms
// Beats
// 22.94%
// Memory
// 7.8 MB
// Beats
// 50.26%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int rob(vector<int> &nums) {
    if (nums.size() == 1)
      return nums[0];
    for (int i = 2; i < nums.size(); ++i) {
      int first = i > 2 ? nums[i - 3] : 0;
      int second = nums[i - 2];
      nums[i] += max(first, second);
    }
    return max(nums[nums.size() - 1], nums[nums.size() - 2]);
  }
};
