// problem:
// https://leetcode.com/problems/find-original-array-from-doubled-array/
// Runtime: 933 ms, faster than 19.04% of C++ online submissions for Find
// Original Array From Doubled Array. Memory Usage: 153.5 MB, less than 21.78%
// of C++ online submissions for Find Original Array From Doubled Array.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<int> findOriginalArray(vector<int> &changed) {
    vector<int> ans;
    sort(changed.begin(), changed.end());
    unordered_map<int, int> counter;
    for (int num : changed)
      counter[num]++;

    for (int num : changed) {
      if (counter[num * 2] && counter[num]) {
        ans.push_back(num);
        counter[num * 2]--;
        counter[num]--;
      }
    }

    for (auto &it : counter) {
      if (it.second)
        return {};
    }

    return ans;
  }
};
