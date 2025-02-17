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
    vll a(n), b(n);
    ll ma1=0,ma2=-1;
    rep(i, 0, n)
    {
        cin >> a[i];
    }
    rep(i, 0, n)
    {
        cin >> b[i];
        ll c=max(a[i],b[i]); 
        if(c>ma1)   {
            ma2=i;
            ma1=c;
        }
    }
    ll k = 0;
    ll d = -1;
    ll l = 0;
    ll r = -1;
    for (ll = n - 1; i >= 0;i--){
        if(a[i]>k){
            l = k;
            r = d;
            k = a[i];
            d = i;
        }
        else if(a[i]>k){
            l = a[i];
            r = i;
        }
    }
    ll g = max(a[r], b[r]);
    ll h = max(a[d], b[d]);
    if (g==h&& h==ma1)
    {
        cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }
}
//  =========================================================================
int main()
{
    IOS;
    ll t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}
