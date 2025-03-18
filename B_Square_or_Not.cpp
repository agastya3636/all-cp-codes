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

void solve()
{
    ll n;
    cin >> n;
    string s;
    cin >> s;

    ll k = sqrt(n);
    if (k * k != n)
    {
        cout << "No" << endl;
        return;
    }

    vector<vi> v(k, vi(k, 0));
    ll l = 0;
    ll c0 = 0;
    rep(i, 0, k)
    {
        rep(j, 0, k)
        {
            v[i][j] = s[l] - '0';
            l++;
            if (v[i][j] == 1)
            {
                c0++;
            }
        }
    }
    rep(i, 0, k)
    {
        if (v[0][i] != 1 || v[i][0] != 1 || v[k - 1][i] != 1 || v[i][k - 1] != 1)
        {
            cout << "No" << endl;
            return;
        }
    }

    if (c0 != (4*k-4))
    {
        cout << "No" << endl;
        return;
    }

    cout << "Yes" << endl;
}
//  =========================================================================
int main()
{
    IOS;
    ll t ;
    cin >> t;
    while (t--)
    {
        solve();
    }
}
