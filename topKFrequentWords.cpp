// problem: https://leetcode.com/problems/top-k-frequent-words/
// Runtime: 36 ms, faster than 15.60% of C++ online submissions for Top K
// Frequent Words. Memory Usage: 12.7 MB, less than 39.56% of C++ online
// submissions for Top K Frequent Words.

#include <bits/stdc++.h>
using namespace std;

bool compare(pair<string, int> &a, pair<string, int> &b) {
  if (a.second != b.second)
    return a.second > b.second;
  return a.first < b.first;
}

class Solution {
public:
  vector<string> topKFrequent(vector<string> &words, int k) {
    unordered_map<string, int> m;
    vector<string> ans;
    for (string word : words) {
      m[word]++;
    }
    vector<pair<string, int>> arr;
    for (auto const &p : m) {
      arr.push_back(p);
    }
    sort(arr.begin(), arr.end(), compare);
    for (auto const &tmp : arr) {
      ans.push_back(tmp.first);
      k--;
      if (k <= 0)
        return ans;
    }
    return ans;
  }
};
