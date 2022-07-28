// problem: https://leetcode.com/problems/valid-anagram/submissions/
// Runtime: 14 ms, faster than 57.46% of C++ online submissions for Valid Anagram.
// Memory Usage: 7.3 MB, less than 45.59% of C++ online submissions for Valid Anagram.

#include <bits/stdc++.h> 

using namespace std;


class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> vs(26, 0), vt(26, 0);
        for (char c: s) ++vs[c - 'a'];
        for (char c: t) ++vt[c - 'a'];
        for (int i = 0; i < 26; ++i) if (vs[i] != vt[i]) return false;
        return true;
    }
};
