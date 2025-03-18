#include <bits/stdc++.h>
#include <functional>
using namespace std;
//===================================================================================================================
//       Agastya Kumar Yadav
//
//
//===================================================================================================================
#define pb push_back
#define mp make_pair
#define ll long long
#define endl '\n'
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define vll vector<ll>
#define vvi vector<vi>
#define vvll vector<vll>
#define vpii vector<pii>
#define vpll vector<pll>
#define srt(v) sort(v.begin(), v.end())
#define desort(v) sort(v.begin(), v.end(), greater<int>())
#define all(x) x.begin(), x.end()
#define rep(i, a, b) for (ll i = a; i < b; i++)
#define repr(i, a, b) for (ll i = a; i >= b; i--)
#define F first
#define S second
#define gcd(a, b) __gcd(a, b)
#define sz(x) (ll) x.size()
#define lbnd lower_bound
#define ubnd upper_bound
#define bs binary_search
#define print(a)     \
    for (auto i : a) \
        cout << i << " ";
#define IOS                      \
    ios::sync_with_stdio(false); \
    cin.tie(0);                  \
    cout.tie(0)

//===========================================================================

const int MOD = 1e9 + 7;

int power(int a, int b)
{
    int res = 1;
    while (b > 0)
    {
        if (b & 1)
        {
            res = (res * 1LL * a) % MOD;
        }
        a = (a * 1LL * a) % MOD;
        b >>= 1;
    }
    return res;
}

int modInverse(int a)
{
    return power(a, MOD - 2);
}

int main()
{
    int t;
    std::cin >> t;
    while (t--)
    {
        int n;
        std::cin >> n;
        std::vector<int> a(n);
        for (int i = 0; i < n; i++)
        {
            std::cin >> a[i];
        }
        int sumSquares = 0;
        int sumProducts = 0;
        for (int i = 0; i < n; i++)
        {
            sumSquares = (sumSquares + 1LL * a[i] * a[i]) % MOD;
            for (int j = i + 1; j < n; j++)
            {
                sumProducts = (sumProducts + 1LL * a[i] * a[j]) % MOD;
            }
        }
        int Q = n * 1LL * (n - 1) / 2 % MOD;
        int P = (sumSquares + 2LL * sumProducts) % MOD;
        P = (P * 1LL * modInverse(Q)) % MOD;
        cout << P <<endl;
    }
    return 0;
}
//  =========================================================================
