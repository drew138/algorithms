// problem: https://leetcode.com/problems/ransom-note/
// Runtime: 18 ms, faster than 74.92% of C++ online submissions for Ransom Note.
// Memory Usage: 8.8 MB, less than 39.49% of C++ online submissions for Ransom
// Note.

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  bool canConstruct(string ransomNote, string magazine) {
    vector<int> a(26, 0), b(26, 0);

    for (int i = 0; i < ransomNote.size(); ++i) {
      a[ransomNote[i] - 'a']++;
    }
    for (int i = 0; i < magazine.size(); ++i) {
      b[magazine[i] - 'a']++;
    }
    for (int i = 0; i < 26; ++i) {
      if (b[i] < a[i])
        return false;
    }
    return true;
  }
};
