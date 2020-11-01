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

// problem: https://leetcode.com/problems/excel-sheet-column-title/submissions/
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Excel Sheet Column Title.
// Memory Usage: 6.5 MB, less than 100.00% of C++ online submissions for Excel Sheet Column Title.
class Solution
{
public:
    string convertToTitle(int n)
    {
        string answer;
        while (n != 0)
        {
            n--;
            answer += ('@' + (n % 26) + 1);
            n = n / 26;
        }
        reverse(answer.begin(), answer.end());
        return answer;
    }
};