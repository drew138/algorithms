// problem: https://leetcode.com/problems/largest-perimeter-triangle/
// Runtime: 91 ms, faster than 20.25% of C++ online submissions for Largest
// Perimeter Triangle. Memory Usage: 22 MB, less than 22.88% of C++ online
// submissions for Largest Perimeter Triangle.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int largestPerimeter(vector<int> &nums) {
    sort(nums.begin(), nums.end(), greater<int>());
    for (int i = 0; i + 2 < nums.size(); ++i) {
      if (nums[i] < nums[i + 1] + nums[i + 2])
        return nums[i] + nums[i + 1] + nums[i + 2];
    }
    return 0;
  }
};
