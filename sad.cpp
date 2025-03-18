#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int minBuses(int N, vector<int> &passengers, vector<vector<int>> &edges)
{
    vector<vector<int>> graph(N + 1);
    vector<int> degree(N + 1, 0);

    // Build adjacency list and track degree of each node
    for (auto &edge : edges)
    {
        int u = edge[0], v = edge[1];
        graph[u].push_back(v);
        graph[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    queue<int> q;

    // Add initial leaf nodes with no passengers to the queue
    for (int i = 2; i <= N; i++)
    { // Ignore node 1 (root)
        if (degree[i] == 1 && passengers[i - 1] == 0)
        {
            q.push(i);
        }
    }

    // Remove all leaf nodes that have no passengers
    while (!q.empty())
    {
        int node = q.front();
        q.pop();

        // Reduce degree of its neighbor (parent)
        for (int neighbor : graph[node])
        {
            degree[neighbor]--;
            if (degree[neighbor] == 1 && passengers[neighbor - 1] == 0)
            {
                q.push(neighbor); // Remove its parent if it's now a leaf and has no passengers
            }
        }
    }

    int buses = 0;

    // Count remaining leaf nodes with passengers
    for (int i = 2; i <= N; i++)
    {
        if (degree[i] == 1 && passengers[i - 1] == 1)
        {
            buses++;
        }
    }

    return buses;
}

int main()
{
    int N = 5;
    vector<int> passengers = {1, 1, 0, 0, 0};
    vector<vector<int>> edges = {{1, 2}, {2, 3}, {2, 4}, {4, 5}};

    cout << minBuses(N, passengers, edges) << endl;
    return 0;
}
