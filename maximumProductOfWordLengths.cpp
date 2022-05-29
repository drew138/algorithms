#include <bits/stdc++.h>


using namespace std;

class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int> vals;
        
        for (string &word: words) {
            int tmp = 0;
            for (char &character: word) {
                tmp |= 1 << (character - 96);
            }
            vals.push_back(tmp);
        }
        int ans = 0, n = vals.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j){
                if (!(vals[i] & vals[j])) {
                    int mult = words[i].length() * words[j].length();
                    ans = max(ans, mult);
                }
            }
        }
        
        return ans;
    }
};