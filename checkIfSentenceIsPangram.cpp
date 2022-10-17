// problem: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Check if the
// Sentence Is Pangram. Memory Usage: 6.6 MB, less than 55.40% of C++ online
// submissions for Check if the Sentence Is Pangram.

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  bool checkIfPangram(string sentence) {
    vector<bool> arr(26, false);
    for (char character : sentence) {
      arr[character - 'a'] = true;
    }
    bool ans = true;
    for (bool val : arr) {
      ans = ans && val;
    }
    return ans;
  }
};
