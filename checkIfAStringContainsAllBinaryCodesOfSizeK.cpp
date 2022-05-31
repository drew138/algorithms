#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool hasAllCodes(string s, int k) {
        if (k > s.size()) return false;
        int cur = 0;
        for (int i = 0; i < k; ++i) {
            cur <<= 1;
            cur |= s[i] - '0';
        }
        vector<bool> seen(1 << k, false);
        seen[cur] = true;
        int tmp = 0;
        for (int i = 0; i < k - 1; ++i){
            tmp <<= 1;
            tmp |= 1;
        }
        for (int i = k; i < s.size(); ++i) {
            cur = cur & tmp;
            cur <<= 1;
            cur |= s[i] - '0';
            seen[cur] = true;
        }
        for (bool val: seen) if (!val) return val;
        
        return true;
    }
};