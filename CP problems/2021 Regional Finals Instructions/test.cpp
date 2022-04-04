#include <bits/stdc++.h>

using namespace std;

int main()
{

    int n;
    cin >> n;
    int sum = 0;
    int a[n];
    for (int i = 0; i < n; i++)
    {

        cin >> a[i];
        sum += a[i];
    }
    sum = sum / n;
    int l = 0, r = 1;
    int cnt = 0;
    int acc = a[0];
    cout << sum << endl;
    while (r < n)
    {
        while (acc / (r - l) >= sum and l < r)
        {
            
            if (acc / (r - l) == sum)
            {
                cnt++;
            }
            acc -= a[l];
            l++;
        }
        acc += a[r];
        r += 1;
        if (acc / (r - l) == sum)
        {
            cnt++;
        }
        cout << acc / (r - l) << " " << l << " " << r << endl;
    }
    cout << cnt;
}