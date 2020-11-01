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

// problem: https://leetcode.com/problems/count-primes/submissions/
// Runtime: 52 ms, faster than 74.55% of C++ online submissions for Count Primes.
// Memory Usage: 33.1 MB, less than 10.18% of C++ online submissions for Count Primes.

class Solution
{
public:
    int countPrimes(int n)
    {
        vector<long> primes(n, 0);
        if ((n == 0) || (n == 1) || (n == 2))
            return 0;
        int numPrimes = 0;
        for (long long i = 2; i < n; ++i)
        {
            if (primes[i])
                continue;
            long long j = i * i;
            while (j < n)
            {
                primes[j] = 1;
                j += i;
            }
            numPrimes++;
        }
        return numPrimes;
    }
};