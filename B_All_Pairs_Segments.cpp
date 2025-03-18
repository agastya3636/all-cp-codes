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
    ll n,m;
    cin >> n>>m;
    map<ll, ll> mp;
    vll v(n);
    rep(i,0,n){
        cin >> v[i];
    }
    vll q(m);
    ll k = n-1;
    rep(i,0,n-1){
        mp[k] += (v[i+1] - v[i ]);
        cout << k << "/" << v[i] << endl;
        k = k + (n - (i+2));
    }
    mp[n-1] += 1;
    rep(i, 0, m)
    {
        cin >> q[i];
        if(mp.find(q[i])!=mp.end())
        {
            cout << mp[q[i]] <<" ";
        }
        else
        {
            cout << 0<< " " ;
        }
    }
    cout << endl;
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
