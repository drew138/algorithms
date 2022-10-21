// problem: https://leetcode.com/problems/contains-duplicate-ii/
// Runtime: 196 ms, faster than 90.56% of C++ online submissions for Contains
// Duplicate II. Memory Usage: 77.2 MB, less than 33.65% of C++ online
// submissions for Contains Duplicate II.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  bool containsNearbyDuplicate(vector<int> &nums, int k) {
    unordered_map<int, int> m;
    for (int i = 0; i < nums.size(); ++i) {
      int num = nums[i];
      if (nums[m[num]] == num && m[num] != i && i - m[num] <= k)
        return true;
      m[num] = i;
    }
    return false;
  }
};
