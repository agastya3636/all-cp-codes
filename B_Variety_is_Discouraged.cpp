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
    vll a(n);
    unordered_map<ll, ll> f;
    rep(i,0,n)
    {
        cin >> a[i];
        f[a[i]]++;
    }
    set<ll> s;
    for (auto it = f.begin(); it != f.end(); ++it)
    {
        if (it->second == 1)
        {
            s.insert(it->first);
        }
    }
    ll m = 0, l1 = -1, r1 = -1, r = 0;

    for (ll l = 0; r < n; r++)
    {
        if (s.find(a[r]) == s.end())
        {
            l = r + 1;
        }
        else
        {
            ll length = r - l + 1;
            if (length > m)
            {
                m = length;
                l1 = l;
                r1 = r;
            }
        }
    }
    if (m==0)
    {
        cout << "0"<<endl;
    }
    else
    {
        cout<<l1+1 << " " <<r1+1<<endl;
    }
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
