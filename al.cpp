#include <iostream>
#include <vector>

using namespace std;

int solve(const vector<int> &arr)
{
    int n = arr.size();
    int total_subarrays = n * (n + 1) / 2; // Total number of subarrays
    int x = 0;
    int y = 0;

    for (int k = 0; k < 31; ++k)
    {

        int cnt_and = 0;
        int current_run = 0;
        for (int num : arr)
        {
            if (num & (1 << k))
            {
                current_run += 1;
                cnt_and += current_run;
            }
            else
            {
                current_run = 0;
            }
        }

        int cnt_or_unset = 0;
        current_run = 0;
        for (int num : arr)
        {
            if (!(num & (1 << k)))
            {
                current_run += 1;
                cnt_or_unset += current_run;
            }
            else
            {
                current_run = 0;
            }
        }

        if (cnt_and % 2 == 1)
        {
            x += (1 << k);
        }
        int or_parity = (total_subarrays - cnt_or_unset) % 2;
        if (or_parity)
        {
            y += (1 << k);
        }
    }

    return x + y;
}

int main()
{
    vector<int> arr1 = {1, 2, 3};
    cout << "Result: " << solve(arr1) << endl; // Expected output: 3

    vector<int> arr2 = {5, 10, 15};
    cout << "Result: " << solve(arr2) << endl; // Expected output: 15

    vector<int> arr3 = {1, 2, 3, 4, 5};
    cout << "Result: " << solve(arr3) << endl; // Expected output: 7

    vector<int> arr4 = {0, 0, 0};
    cout << "Result: " << solve(arr4) << endl; // Expected output: 0

    vector<int> arr5 = {1, 0, 1, 0, 1};
    cout << "Result: " << solve(arr5) << endl; // Expected output: 7

    vector<int> arr6 = {7, 6, 5, 4, 3, 2, 1};
    cout << "Result: " << solve(arr6) << endl; // Expected output: 7

    return 0;
}
