string solve(int n, int m, vector<vector<int>> A)
{
    
    vector<vector<int>> v;

    for (int i = 0; i < n; i++)
    {
        int d=A[i][0], s1=A[i][1], s2=A[i][2], s3=A[i][3];;
        v.push_back({s1, s1 + d, i});
        v.push_back({s2, s2 + d, i});
        v.push_back({s3, s3 + d, i});
    }

    sort(v.begin(), v.end());

    unordered_set<int> used;
    return (dfs(0, m, v, used) ? "YES" : "NO") ;
}