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

// problem: https://leetcode.com/problems/buddy-strings/submissions/
// Runtime: 12 ms, faster than 10.61% of C++ online submissions for Buddy Strings.
// Memory Usage: 7.2 MB, less than 6.17% of C++ online submissions for Buddy Strings.

class Solution
{
public:
    bool buddyStrings(string A, string B)
    {
        if (A.length() != B.length())
        {
            return false;
        }
        vector<char> characters;
        set<char> seen, repeated;
        for (int i = 0; i < A.length(); ++i)
        {
            if (A.at(i) != B.at(i))
            {
                characters.push_back(A.at(i));
                characters.push_back(B.at(i));
            }
            if (seen.find(A.at(i)) != seen.end())
            {
                repeated.insert(A.at(i));
            }
            else
            {
                seen.insert(A.at(i));
            }
        }
        if ((characters.size() != 4) && (characters.size() != 0))
        {
            return false;
        }
        else if (characters.size() == 0)
        {
            return !repeated.empty();
        }
        else
        {
            return ((characters[0] == characters[3]) && (characters[1] == characters[2]));
        }
    }
};