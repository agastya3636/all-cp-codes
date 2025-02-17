#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;
typedef vector<ll> vll;

bool is_valid(int x, int y, int n, int m)
{
    return x >= 0 && x < n && y >= 0 && y < m;
}

bool is_stable(const vector<string> &grid, int x, int y, int n)
{
    if (x == n - 1) // Last row
        return true;
    return x + 1 < n && grid[x + 1][y] == 'B'; // There is a building below
}

vector<pii> get_valid_moves(int x, int y, const vector<string> &grid, int n, int m)
{
    vector<pii> valid_moves;
    vector<pii> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    for (auto i : directions)
    {
        auto dx = i.first , dy = i.second;
        int new_x = x + dx, new_y = y + dy;
        if (is_valid(new_x, new_y, n, m) && grid[new_x][new_y] != 'B')
        {
            valid_moves.push_back({new_x, new_y});
        }
    }
    return valid_moves;
}

pii apply_gravity(const vector<string> &grid, int x, int y, int n)
{
    int original_x = x;
    while (x < n - 1 && !is_stable(grid, x, y, n))
    {
        x++;
        if (x < n && grid[x][y] == 'B')
        {
            x--;
            break;
        }
    }
    return {x, y}; // Return final position
}

int manhattan_distance(int x1, int y1, int x2, int y2)
{
    return abs(x1 - x2) + abs(y1 - y2);
}

vector<pii> find_farthest_reach(int n, int m, const vector<string> &grid, int k)
{
    int start_x = -1, start_y = -1;

    // Find start position 'S'
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (grid[i][j] == 'S')
            {
                start_x = i;
                start_y = j;
                break;
            }
        }
        if (start_x != -1)
            break;
    }

    // Apply gravity to starting position
    auto final = apply_gravity(grid, start_x, start_y, n);
    auto final_x=final.first;
    auto final_y=final.second;
    deque<vll> queue; // (x, y, steps)
    queue.push_back({final_x, final_y, 0});

    map<pii, int> visited; // (x, y) -> minimum steps to reach
    visited[{final_x, final_y}] = 0;

    int max_distance = -1;
    vector<pii> result_cells;

    while (!queue.empty())
    {
        auto f = queue.front();
        queue.pop_front();
        auto x = f[0], y = f[1], steps = f[2];

        if (steps > k)
            continue;

        if (visited[{x, y}] != 0 && visited[{x, y}] <= steps)
            continue;

        visited[{x, y}] = steps;

        // If stable and not a building, check distance
        if (is_stable(grid, x, y, n) && grid[x][y] != 'B')
        {
            int dist = manhattan_distance(start_x, start_y, x, y);
            if (dist > max_distance)
            {
                max_distance = dist;
                result_cells = {{x, y}};
            }
            else if (dist == max_distance)
            {
                result_cells.push_back({x, y});
            }
        }

        // Try each valid move
        for (auto next : get_valid_moves(x, y, grid, n, m))
        {
            auto next_x = next.first, next_y = next.second;
            auto final = apply_gravity(grid, next_x, next_y, n);
            auto final_x=final.first;
            auto final_y=final.second;
            if (steps + 1 <= k && visited[{final_x, final_y}] == 0)
            {
                queue.push_back({final_x, final_y, steps + 1});
            }
        }
    }

    sort(result_cells.begin(), result_cells.end());
    return result_cells;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, k;
    cin >> n >> m;
    vector<string> grid(n);
    for (int i = 0; i < n; i++)
    {
        cin >> grid[i];
    }
    cin >> k;
    vector<pii> result = find_farthest_reach(n, m, grid, k);
    for (auto i : result)
    {
        cout << i.first << " " << i.second << "\n";
    }

    return 0;
}
