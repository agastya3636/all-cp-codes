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
    ll n, k;
    cin >> n >> k;
    vll a(n);
    rep(i, 0, n) cin >> a[i];

    ll mn = a[0], mx = a[0];
    rep(i, 1, n)
    {
        if (a[i] < mn)
            mn = a[i];
        if (a[i] > mx)
            mx = a[i];
    }

    ll l = 0, r = mx - mn;
    while (l < r)
    {
        ll mid = (l + r) / 2;
        ll c = 1;
        ll m_v = a[0] - mid;
        ll ma_v = a[0] + mid;

        rep(i,1,n)
        {
            ll nl = a[i] - mid;
            ll nh = a[i] + mid;
            m_v = max(m_v, nl);
            ma_v = min(ma_v, nh);

            if (m_v > ma_v)
            {
                c++;
                m_v = nl;
                ma_v = nh;
            }
        }

        if (c <= k + 1)
        {
            r = mid;
        }
        else
        {
            l = mid + 1;
        }
    }

    cout << l << endl;
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
