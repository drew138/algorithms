#include <bits/stdc++.h>

#define D(x) cout << #x << " = " << x << endl;
#define ios ios_base::sync_with_stdio(0), cin.tie(0);
#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define all(v) v.begin(), v.end()
#define allgreater(v) v.begin(), v.end(), greater<int>()
#define formap(map) for (const auto &[key, value] : map)
#define ms(ar, val) memset(ar, val, sizeof ar)
typedef long long ll;
typedef long double ld;

using namespace std;

// problem: https://leetcode.com/problems/longest-common-prefix/submissions/
// Runtime: 4 ms, faster than 96.65% of C++ online submissions for Longest Common Prefix.
// Memory Usage: 9.7 MB, less than 7.18% of C++ online submissions for Longest Common Prefix.

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.empty())
        {
            return "";
        }
        string prefix = strs[0];
        for (int i = 0; i < strs.size(); ++i)
        {
            prefix = prefix.substr(0, min(prefix.length(), strs[i].length()));
            for (int j = 0; j < prefix.length(); ++j)
            {
                if (strs[i][j] != prefix[j])
                {
                    prefix = prefix.substr(0, j);
                    break;
                }
            }
            if (prefix == "")
                return "";
        }
        return prefix;
    }
};