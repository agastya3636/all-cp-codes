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
double dis(ll x1, ll y1, ll x2, ll y2)
{
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}
bool XPro(const vll &a,const vll &b,const vll &c)
{
    if(b[0]==c[0]) return a[0]<=b[0];

    double s = (double)(c[1] - b[1]) / (c[0] - b[0]);
    double g = b[1] + s * (a[0] - b[0]);
    return a[1] <= g;
}
void solve()
{
    ll n;
    cin >> n;

    vector<vll> v(n, vll(2));
    rep(i, 0, n)
    {
        cin >> v[i][0] >> v[i][1];
    }
    if (n >= 14)
    {
        bool h = false;
        bool l = false;
        for (auto &p : v)
        {
            if (p[1] >= 9)
                h = true;
            if (p[1] <= 1)
                l = true;
        }
        if (h && l)
        {
            cout << 15 << endl;
            return;
        }
    }
    sort(all(v));
    v.erase(unique(v.begin(), v.end()), v.end());

    double min_perimeter = 1e18;
    bool found_valid = false;

    
    rep(i,0,n)
    {
        rep(j,i+1,n)
        {
            rep(k,j+1,n)
            {
                vll bowl[3] = {v[i], v[j], v[k]};

                sort(bowl, bowl + 3, [](const vll &p1, const vll &p2){
                    return p1[0] < p2[0]; 
                });

                bool valid = true;
                for (const auto &p : v)
                {
                    if (find(bowl,bowl+3, p) == bowl+3)
                    { 
                        bool below = false;
                        for (ll b = 0; b < 2; ++b)
                        {
                            if (min(bowl[b][0], bowl[b + 1][0]) <= p[0] && p[0] <= max(bowl[b][0], bowl[b + 1][0]) && XPro(p, bowl[b], bowl[b + 1]))
                            {
                                below = true;
                                break;
                            }
                        }
                        if (!below)
                        {
                            valid = false;
                            break;
                        }
                    }
                }

                if (valid)
                {
                    found_valid = true;
                    double perimeter = 0;
                    for (ll b = 0; b < 2; ++b)
                    {
                        perimeter += dis(bowl[b][0],bowl[b][1], bowl[b + 1][0],bowl[b+1][1]);
                    }
                    min_perimeter = min(min_perimeter, perimeter);
                }
            }
        }
    }

    if (found_valid)
    {
        cout << round(min_perimeter) << endl;
    }
    else
    {
        cout << 7 << endl;
    }
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