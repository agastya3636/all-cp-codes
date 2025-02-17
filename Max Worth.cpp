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
ll worth_word(string s)
{
    ll c = 0;
    for(auto i : s)
    {
        c += (i - 'a') + 1;
    }
    return c;
}

void backtrack(ll pos, ll remaining_budget, vll &selected, ll &max_worth, const vll &worth, const vll &costs, const vector<unordered_set<int>> &contra_map, ll n)
{
    if (pos == n)
    {
        ll current_worth = 0;
        for (ll idx : selected)
        {
            current_worth += worth[idx];
        }
        max_worth = max(max_worth, current_worth);
        return;
    }

    backtrack(pos + 1, remaining_budget, selected, max_worth, worth, costs, contra_map, n);

    if (costs[pos] <= remaining_budget)
    {
        bool can_include = true;
        for (ll idx : selected)
        {
            if (contra_map[idx].count(pos))
            {
                can_include = false;
                break;
            }
        }
        if (can_include)
        {
            selected.push_back(pos);
            backtrack(pos + 1, remaining_budget - costs[pos], selected, max_worth, worth, costs, contra_map, n);
            selected.pop_back();
        }
    }
}

void solve()
{
    ll n, m;
    cin >> n >> m;
    vector<string> s(n);
    vll costs(n, 0);
    vll worth(n);
    unordered_map<string, int> str_to_idx;

    for (int i = 0; i < n; ++i)
    {
        cin >> s[i];
        str_to_idx[s[i]] = i;
        worth[i] = worth_word(s[i]);
    }

    for (int i = 0; i < n; ++i)
    {
        cin >> costs[i];
    }

    vector<unordered_set<int>> ma(n);
    for (int i = 0; i < m; ++i)
    {
        string x, y;
        cin >> x >> y;
        int idx1 = str_to_idx[x];
        int idx2 = str_to_idx[y];
        ma[idx1].insert(idx2);
        ma[idx2].insert(idx1);
    }

    ll budget;
    cin >> budget;
    ll max_worth = 0;
    vll selected;
    backtrack(0, budget, selected, max_worth, worth, costs, ma, n);

    cout << max_worth << endl;
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

