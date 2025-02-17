#include <iostream>
#include <vector>
#include <map>

using namespace std;

// Function to perform DFS and calculate maximum squads
void dfs(int node, const vector<vector<int>> &tree, int &total_squads, int &unpaired)
{
    // Process each child
    for (int child : tree[node])
    {
        int child_squads = 0;
        int child_unpaired = 0;
        dfs(child, tree, child_squads, child_unpaired);
        total_squads += child_squads;
        unpaired += child_unpaired;
    }

    // Form pairs from unpaired knights
    total_squads += unpaired / 2;
    unpaired = unpaired % 2; // Remaining unpaired knights
}

// Main function to find the maximum number of squads
int maxSquads(const vector<int> &arr)
{
    int n = arr.size() + 1; // Number of knights
    vector<vector<int>> tree(n);

    // Build the tree
    for (int i = 1; i < n; ++i)
    {
        tree[arr[i - 1]].push_back(i);
    }

    int total_squads = 0;
    int unpaired = 0;

    // Start DFS from the King (node 0)
    dfs(0, tree, total_squads, unpaired);

    return total_squads;
}

int main()
{
    // Test case 1
    vector<int> arr1 = {0, 0, 2, 1, 1, 3};
    cout << "Knight Squads: " << maxSquads(arr1) << endl; // Expected Output: 3

    // Test case 2
    vector<int> arr2 = {0, 0, 0, 0, 0};
    cout << maxSquads(arr2) << endl; // Output: 2

    // Test case 3
    vector<int> arr3 = {0, 1, 2, 3};
    cout << maxSquads(arr3) << endl; // Output: 0

    // Test case 4
    vector<int> arr4 = {0, 0, 1, 1};
    cout << maxSquads(arr4) << endl; // Output: 1

    // Test case 5
    vector<int> arr5 = {0, 1, 0, 3, 0};
    cout << maxSquads(arr5) << endl; // Output: 2

    // Test case 6
    vector<int> arr6 = {0};
    cout << maxSquads(arr6) << endl; // Output: 1

    // Test case 7
    vector<int> arr7 = {};
    cout << maxSquads(arr7) << endl; // Output: 0

    // Test case 8
    vector<int> arr8 = {0, 1, 0, 2};
    cout << maxSquads(arr8) << endl; // Output: 1

    return 0;
}
