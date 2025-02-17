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
    vll v(n,1);
    if(n<4||(n%2==1&&n<=25))
    {
        cout << -1 << endl;
    }
    else {
        if(n%2==0)
        {
            rep(i,0,n/2)
            {
                cout << i+1 << " " << i+1 << " ";
            }
        }
        else {
            vll v(n,0);
            v[1-1] = 1;
            v[10-1] = 1;
            v[25-1] = 1;
            ll k = 2;
            rep(i,1,9)
            {
                
                v[i] = k;
                i++;
                v[i] = k;
                k++;
            }
            rep(i,10,24)
            {
                v[i] = k;
                i++;
                v[i] = k;
                k++;
            }
            rep(i,25,n)
            {
                v[i] = k;
                i++;
                v[i] = k;
                k++;
            }
            rep(i,0,n)
            {
                cout << v[i] << " ";
            }
            cout << endl;
        }
        
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
