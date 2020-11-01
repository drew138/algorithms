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

// problem: https://leetcode.com/problems/reverse-words-in-a-string/submissions/
// Runtime: 4 ms, faster than 96.74% of C++ online submissions for Reverse Words in a String.
// Memory Usage: 7.7 MB, less than 5.08% of C++ online submissions for Reverse Words in a String.

class Solution
{
public:
    string reverseWords(string s)
    {
        int numChars = s.length();
        bool hasPrevBlank = true;
        int l, r;
        string answer = "";
        vector<pair<int, int>> indexes;
        while (numChars--)
        {
            if (s.at(numChars) != ' ')
            {
                if (hasPrevBlank)
                {
                    r = numChars;
                }
                l = numChars;
                hasPrevBlank = false;
            }
            else
            {
                if (!hasPrevBlank)
                {
                    indexes.push_back(std::make_pair(l, 1 + r - l));
                    hasPrevBlank = true;
                }
            }
        }
        if (s.at(0) != ' ')
        {
            indexes.push_back(std::make_pair(l, 1 + r - l));
        }
        for (int i = 0; i < indexes.size(); i++)
        {
            if (i == 0)
            {
                answer += s.substr(indexes[i].first, indexes[i].second);
            }
            else
            {
                answer += " " + s.substr(indexes[i].first, indexes[i].second);
            }
        }
        return answer;
    }
};