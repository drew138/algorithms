// problem: https://leetcode.com/problems/find-k-closest-elements/
// Runtime: 228 ms, faster than 5.93% of C++ online submissions for Find K
// Closest Elements. Memory Usage: 33.9 MB, less than 46.76% of C++ online
// submissions for Find K Closest Elements.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<int> findClosestElements(vector<int> &arr, int k, int x) {
    priority_queue<pair<int, int>> pq;
    vector<int> ans;
    for (int num : arr) {
      pq.push({abs(num - x), num});
      while (pq.size() > k)
        pq.pop();
    }
    while (pq.size()) {
      auto element = pq.top();
      pq.pop();
      ans.push_back(element.second);
    }

    sort(ans.begin(), ans.end());
    return ans;
  }
};
