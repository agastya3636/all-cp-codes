#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;
int matrixChainMultiplication(vector<int> &p)
{
    int n = p.size() - 1;                         
    vector<vector<int>> dp(n, vector<int>(n, 0)); 
  
    for (int l = 2; l <= n; ++l)
    {
        for (int i = 0; i <= n - l; ++i)
        {
            int j = i + l - 1;
            dp[i][j] = INT_MAX; 
            for (int k = i; k < j; ++k)
            {
                int cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1];
                if (cost < dp[i][j])
                {
                    dp[i][j] = cost;
                }
            }
        }
    }
    return dp[0][n - 1];
}
int main()
{
    vector<int> dimensions = {10, 20, 30, 40, 30};
    int result = matrixChainMultiplication(dimensions);
    cout << "Minimum number of multiplications is: " << result << endl;
    return 0;
}
