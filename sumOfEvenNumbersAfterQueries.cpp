// problem: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
// Runtime: 119 ms, faster than 88.10% of C++ online submissions for Sum of Even
// Numbers After Queries. Memory Usage: 46.1 MB, less than 66.47% of C++ online
// submissions for Sum of Even Numbers After Queries.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<int> sumEvenAfterQueries(vector<int> &nums,
                                  vector<vector<int>> &queries) {
    int total = 0;
    vector<int> ans;
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] % 2 == 0)
        total += nums[i];
    }
    cout << total << endl;
    for (vector<int> &arr : queries) {
      if ((nums[arr[1]] + arr[0]) % 2 == 0) {
        total += nums[arr[1]] % 2 == 0 ? arr[0] : nums[arr[1]] + arr[0];
      } else {
        total += nums[arr[1]] % 2 == 0 ? -nums[arr[1]] : 0;
      }
      nums[arr[1]] += arr[0];
      ans.push_back(total);
    }
    return ans;
  }
};
