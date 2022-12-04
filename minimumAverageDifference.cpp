// problem:
// https://leetcode.com/problems/minimum-average-difference/submissions/
// Runtime: 135 ms, faster than 87.64% of C++ online submissions for Minimum
// Average Difference. Memory Usage: 84.6 MB, less than 37.74% of C++ online
// submissions for Minimum Average Difference.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int minimumAverageDifference(vector<int> &nums) {
    long long total = 0;
    for (int i = 0; i < nums.size(); ++i) {
      total += nums[i];
    }
    vector<long long> prefix(nums.size());
    prefix[0] = nums[0];
    for (int i = 1; i < prefix.size(); ++i)
      prefix[i] = nums[i] + prefix[i - 1];

    long long ans = 0;
    long long cur = INT_MAX;
    for (int i = 0; i < prefix.size(); ++i) {
      long long left = prefix[i];
      long long right = total - left;
      left /= (i + 1);

      if (((prefix.size()) - (i + 1)) == 0) {
        right = 0;
      } else {

        right /= (prefix.size() - (i + 1));
      }

      if (abs(right - left) < cur) {
        ans = i;
        cur = abs(right - left);
      }
    }
    return ans;
  }
};
