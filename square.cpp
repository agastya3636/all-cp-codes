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
bool compare(const vll &a, const vll &b) {
return (a[0] - a[1]) < (b[0] - b[1]);
}

void solve()
{
    ll n, m;
    cin >> n >> m;

    vvll c(n, vll(2));
    rep(i, 0, n) cin >> c[i][0];
    rep(i, 0, n) cin >> c[i][1];

    sort(c.begin(), c.end(), [](const vll &a, const vll &b)
         { return (a[0] - a[1]) < (b[0] - b[1]); }
    );

    ll ans = 0;

    for (const auto &e : c)
    {
        ll cx = e[0], r = e[1];

        for (ll dx = -r; dx <= r; dx++)
        {
            ll maxY = (ll)sqrt(r * r - dx * dx);
            ans += (2 * maxY + 1);
        }
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
