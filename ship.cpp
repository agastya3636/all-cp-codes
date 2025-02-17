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
class System
{
public:
    map<string, vector<string>> rgrph;
    map<string, int> swch_cnt;
    map<string, string> crnt_paths;
    int max_swchs;
    vector<int> mnl_costs;
    map<string, vector<string>> paths_2_whs;

    void add_conn(const string &frm, const vector<string> &to)
    {
        for (size_t i = 0; i < to.size(); ++i)
        {
            rgrph[to[i]].push_back(frm);
        }
    }

    vector<string> find_path(const string &gate, const string &whs)
    {
        if (paths_2_whs.find(gate) != paths_2_whs.end())
        {
            return paths_2_whs[gate];
        }

        set<string> vis;
        deque<pair<string, vector<string>>> q;
        q.push_back(mp(gate, vector<string>(1, gate)));

        while (!q.empty())
        {
            pair<string, vector<string>> curr = q.front();
            q.pop_front();

            string node = curr.first;
            vector<string> path = curr.second;

            if (node == whs)
            {
                paths_2_whs[gate] = vector<string>(path.rbegin(), path.rend());
                return paths_2_whs[gate];
            }

            for (size_t i = 0; i < rgrph[node].size(); ++i)
            {
                string nxt_node = rgrph[node][i];
                if (vis.find(nxt_node) == vis.end())
                {
                    vis.insert(nxt_node);
                    vector<string> new_path = path;
                    new_path.push_back(nxt_node);
                    q.push_back(mp(nxt_node, new_path));
                }
            }
        }

        return vector<string>();
    }

    int process_item(const string &gate, const string &whs, int idx)
    {
        vector<string> path = find_path(gate, whs);
        if (path.empty())
        {
            return mnl_costs[idx];
        }

        for (size_t i = 0; i < path.size() - 1; ++i)
        {
            const string &jnct = path[i];
            const string &nxt_node = path[i + 1];

            if (crnt_paths[jnct] != nxt_node)
            {
                if (swch_cnt[jnct] >= max_swchs)
                {
                    return mnl_costs[idx];
                }

                crnt_paths[jnct] = nxt_node;
                swch_cnt[jnct]++;
            }
        }

        return 0;
    }
};
void solve()
{
    int N;
    cin >> N;
    cin.ignore();

    System sys;
    string whs;
    vector<pair<string, vector<string>>> cons;

    for (size_t i = 0; i < N; ++i)
    {
        string line;
        getline(cin, line);
        istringstream iss(line);
        string jct;
        iss >> jct;
        vector<string> cnctd_nodes;
        string node;
        while (iss >> node)
        {
            cnctd_nodes.push_back(node);
        }
        cons.push_back(mp(jct, cnctd_nodes));
        if (jct == "warehouse")
        {
            whs = jct;
        }
    }

    for (size_t i = 0; i < cons.size(); ++i)
    {
        sys.add_conn(cons[i].first, cons[i].second);
    }

    string seq_line;
    getline(cin, seq_line);
    istringstream seq_stream(seq_line);
    vector<string> seq;
    string gate;
    while (seq_stream >> gate)
    {
        seq.push_back(gate);
    }

    string costs_line;
    getline(cin, costs_line);
    istringstream costs_stream(costs_line);
    sys.mnl_costs.clear();
    int cost;
    while (costs_stream >> cost)
    {
        sys.mnl_costs.push_back(cost);
    }

    cin >> sys.max_swchs;

    int total_cost = 0;
    for (size_t i = 0; i < seq.size(); ++i)
    {
        total_cost += sys.process_item(seq[i], whs, i);
    }

    cout << total_cost << endl;
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
