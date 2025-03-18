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
    string s;
    cin >> s;
    ll sum = 0;
    int c = 0;
    for(auto i:s)
    {
        if(i=='+')
            c++;
    }
    ll a = 0, b = 0;
    int d = c;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]!='+')
        {
            a = a * 10 + (s[i] - '0');
        }
        else{
            if(c>1)
            {
                sum += a + (s[i + 1] - '0');
                i++;
            }
                else sum += a;
                c--;
               
                a = 0;
            
        }
    }

    sum += a;
    int m = 0;
    a = 0;
    for (int i = 0; i < s.length();i++)
    {
        if(s[i]=='+')
        {
            if(m==0)
            {
                b += a;
            }
            else{
                b += a / 10 + (a % 10);
            }
            a = 0;
            m++;
            
        }
        else
        {
            a = a * 10 + (s[i] - '0');
        }
    }
    b += a;
    sum = max(b, sum);
    cout << sum << endl;
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
