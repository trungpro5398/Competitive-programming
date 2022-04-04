#include <bits/stdc++.h>

using namespace std;
int main()
{

    int n;
    cin >> n;
    n -= 1;
    int a[(int)(2 << n)];
    for (int i = 0; i < (2 << n)-1; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < (int)(2 << n)-1; i++)
    {
        int l = 0, temp = a[i] ^ 1, res = 0;
       
        for (int j = i; l < (int)(2 << n) -1; j++)
        {   
            
            if ((a[j % ((2 << n)-1)] ^ (l+1)) == temp)
            {
                l++;
                continue;
            }
            res = 1;
            break;
        }
        if (res == 0)
        {
            cout << temp << endl;
            break;
        }
    }
}