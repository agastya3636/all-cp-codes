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
    ll h, w, x, y;
    cin >> h >> w >> x >> y;
    x--;
    y--;
    vector<vector<char>> v(h,vector<char>(w));
    rep(i,0,h)
    {
        rep(j,0,w)
        {
            char d;
            cin >> d;
            v[i][j] = d;
        }
    }
    string s ;
    cin >> s;
    // cout << s;
    ll a = 0;
    for(char i:s)
    {
        if(i == 'U'&&x-1>=0&&v[x-1][y]!='#')
        {
            x--;
            if(v[x][y]=='@')
                a++;
            v[x][y] = '.';
        }
        else if(i == 'D'&&x+1<h&&v[x+1][y]!='#'){
            x++;
            if(v[x][y]=='@')
            a++;
            v[x][y] = '.';
        }
        else if(i == 'L'&&y-1>=0&&v[x][y-1]!='#'){
            y--;
            if(v[x][y]=='@')
            a++;
            v[x][y] = '.';
        }
        else if(i == 'R'&&y+1<w&&v[x][y+1]!='#'){
            y++;
            if(v[x][y]=='@')
            a++;
            v[x][y] = '.';
        }
    }
    cout <<x+1<<" "<<y+1<<" "<< a << "\n";
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
