// problem: https://leetcode.com/problems/search-insert-position/description/
// 0 ms
// Beats
// 100%
// Memory
// 9.6 MB
// Beats
// 96.30%

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int searchInsert(vector<int> &nums, int target) {
    return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
  }
};
