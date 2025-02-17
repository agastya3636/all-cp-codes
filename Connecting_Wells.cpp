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
    vector<vll> v(n);
    rep(i,0,n){
        ll x, y;
        cin >> x >> y;
        v[i].pb({x,y});
    }
    vector<vll> d(n, vll(n, INT_MAX));
    rep(i,0,n)
    {
        rep(j,i+1,n)
        {
            
            ll x = v[i][0], y = v[i][1];
            ll x1 = v[j][0], y1 = v[j][1];
            ll dist = abs(x - x1) + abs(y - y1);
            d[i][j] = dist;
        }
    }
    // implemrnt spanning tree
    vector<vi> adj(n);
    rep(i,0,n)
    {
        rep(j,i+1,n)
        {
            if (d[i][j] != INT_MAX)
            {
                adj[i].pb(j);
                adj[j].pb(i);
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
