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
    ll n, x, y;
    cin >> n >> x >> y;
    vll v(n);
    ll s = 0;
    rep(i, 0, n)
    {
        cin >> v[i];
        s += v[i];
    }
    if (s < x)
    {
        cout << 0 << endl;
        return;
    }
    ll ans = 0;
    sort(all(v));
    ll mi = s - y;
    ll ma = s - x;
    rep(i, 0, n)
    {
        ll f1 = mi - v[i];
        ll f2 = ma - v[i];
        ll l = lower_bound(v.begin() + i + 1, v.end(), f1) - v.begin();
        ll r = upper_bound(v.begin() + i + 1, v.end(), f2) - v.begin() - 1;
        if (l <= r)
            ans += (r - l + 1);
    }
    cout << ans << endl;
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
