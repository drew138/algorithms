// problem:
// https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
// Runtime
// 51 ms
// Beats
// 87.90%
// Memory
// 30.2 MB
// Beats
// 86.10%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int subarraysDivByK(vector<int> &nums, int k) {
    int n = nums.size();
    int curr = 0;
    vector<int> counter(k, 0);
    counter[0] = 1;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      curr = (curr + nums[i] % k + k) % k;
      ans += counter[curr];
      ++counter[curr];
    }
    return ans;
  }
};
