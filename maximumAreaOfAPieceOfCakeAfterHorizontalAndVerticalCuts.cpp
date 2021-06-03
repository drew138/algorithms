// problem: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
// Runtime: 80 ms, faster than 12.90% of C++ online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
// Memory Usage: 32.3 MB, less than 16.10% of C++ online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.

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

int main()
{
}

typedef long long ll;
const int MOD = 1e9 + 7;
class Solution
{
public:
    int maxArea(int h, int w, vector<int> &horizontalCuts, vector<int> &verticalCuts)
    {
        ll prev = 0;
        horizontalCuts.push_back(h);
        verticalCuts.push_back(w);
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());
        ll mw = 0, mh = 0;
        for (auto const &element : horizontalCuts)
        {
            mh = max(mh, element - prev);
            prev = element;
        }
        prev = 0;
        for (auto const &element : verticalCuts)
        {
            mw = max(mw, element - prev);
            prev = element;
        }
        return (mh * mw) % MOD;
    }
};