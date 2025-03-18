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
    ll n, h, b;
    cin >> n >> h >> b;
    vector<vector<char>> v(2, vector<char>(n));

    ll k = 0;
    rep(i, 0, 2)
    {
        rep(j, 0, n)
        {
            cin >> v[i][j];
            if(v[i][j]=='S')
            {
                k=i;
            }
        }
    }
    ll a = 0;
    ll d = 0, w = 0;
    rep(i,0,k)
    {
        if(v[0][i]=='W')
            w++;
        else
            d++;

        if(v[1][i]=='W')
            w++;
        else
            d++;
    }
    a = a + min(h * w, b * d);

     d = 0, w = 0;
    rep(i, k+1, n)
    {
        if (v[0][i] == 'W')
            w++;
        else
            d++;

        if (v[1][i] == 'W')
            w++;
        else
            d++;
    }
    a = a + min(h * w, 2 * d);

    if(v[0][k]=='W'||v[1][k]=='W')
        a += h;
    if(v[0][k]=='.'||v[1][k]=='.')
        a += b;
    cout << a << endl;
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
