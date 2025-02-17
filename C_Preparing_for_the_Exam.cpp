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
    ll n, m, k;
    cin >> n >> m >> k;
    vll v(m);
    rep(i, 0, m) cin >> v[i];
    vll kn(n+1, 0);
    rep(i, 0, k) {
        ll a;
        cin >> a;
        kn[a] = 1;
    }
    // print(kn);
    string s;
    // cout << 1 << endl;
    if(n==k)
    {
        rep(i,0,m)
        {
            s += '1';
        }
        cout << s << endl;
        return;
    }
    else if(n-k>1)
    {
        rep(i, 0, m)
        {
            s += '0';
        }
        cout << s << endl;
        return;
    }
    

    for(int i:v)
    {
        if(kn[i] == 0)
        s += '1';
        else
        s += '0';
    }
    cout << s << endl;
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
