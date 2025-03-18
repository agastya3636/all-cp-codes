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

ll ch(string s)
{
    vi ve(26, 0), vo(26, 0);
    ll cnt = 0;
    ll n = sz(s);   
    rep(i, 0, n)
    {
        if(i%2)
        {
            ve[s[i]-'a']++;
        }
        else
        {
            vo[s[i]-'a']++;
        }
        
    }
    rep(i, 0, 26)
    {
        cnt += ve[i]+vo[i];
    }
    return cnt-*max_element(all(ve))-*max_element(all(vo));
}
void solve()
{
    ll n;
    cin >> n;
    string s;
    cin >> s;
    ll c = INT_MAX;
    if(n%2)
    {
        rep(i,0,n)
        {
            string k = s.substr(0, i) + s.substr(i + 1);
            c = min(c, ch(k));
        }
        c++;
    }
    else
    {
        c = ch(s);
    }
    cout << c << endl;
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
