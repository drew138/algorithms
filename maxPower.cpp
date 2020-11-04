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

// problem: https://leetcode.com/problems/consecutive-characters/submissions/
// Runtime: 4 ms, faster than 86.83% of C++ online submissions for Consecutive Characters.
// Memory Usage: 7.4 MB, less than 100.00% of C++ online submissions for Consecutive Characters.

class Solution
{
public:
    int maxPower(string s)
    {
        int power = 1, cur = 1;
        char prev = s[0];
        for (int i = 1; i < s.size(); ++i)
        {
            if (s[i] == prev)
                cur++;
            else
                cur = 1;
            power = max(power, cur);
            prev = s[i];
        }
        return power;
    }
};