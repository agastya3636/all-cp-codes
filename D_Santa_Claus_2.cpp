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
struct pair_hash
{
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2> &p) const
    {
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ (hash2 << 1); 
    }
};
void solve()
{
    ll n, m, sx, sy;
    cin >> n >> m >> sx >> sy;
    unordered_map<pair<ll,ll>, ll,pair_hash> v;
    rep(i,0,n)
    {
        ll x, y;
        cin >> x >> y;
        v[{x,y}] = 1;
    }
    ll ans = 0;
    rep(i,0,m){
        char d;
        ll c;
        cin >> d >> c;
        if(d=='U')
        {
            sy += c;
            rep(g,0,c)
            {
                if(v[{sx,sy-g}]==1)
                {
                    ans++;
                    v[{sx, sy}] == 0;
                }
            }
        }
        else if(d=='D')
        {
            sy -= c;
            if (v[{sx, sy}] == 1)
            {
                ans++;
                v[{sx, sy}] = 0;
            }
        }
        else if(d=='L')
        {
            sx -= c;
            if (v[{sx, sy}] == 1)
            {
                ans++;
                v[{sx, sy}] = 0;
            }
        }
        else if(d=='R')
        {
            sx += c;
            if (v[{sx, sy}] == 1)
            {
                ans++;
                v[{sx, sy}] = 0;
            }
        }
    }
    cout <<sx<<" "<<sy<<" "<< ans << endl;
}
//  =========================================================================
int main()
{
    IOS;
    ll t =1;
    // cin >> t;
    while (t--)
    {
        solve();
    }
}
