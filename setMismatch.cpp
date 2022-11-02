// problem: https://leetcode.com/problems/set-mismatch/submissions/
// Runtime: 93 ms, faster than 38.16% of C++ online submissions for Set
// Mismatch. Memory Usage: 21.4 MB, less than 66.56% of C++ online submissions
// for Set Mismatch.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<int> findErrorNums(vector<int> &nums) {
    int n = nums.size();
    int total = (n * (n + 1)) / 2;
    sort(nums.begin(), nums.end());
    int ans = 0;
    total -= nums[0];
    for (int i = 1; i < n; ++i) {
      if (nums[i] == nums[i - 1])
        ans = nums[i];
      total -= nums[i];
    }
    return vector<int>{ans, ans + total};
  }
};
