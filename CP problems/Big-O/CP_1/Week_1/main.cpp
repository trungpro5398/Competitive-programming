#include <iostream>

using namespace std;


int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; i += 1){
        int n, m;
        cin >> n>> m;
        int power = 1, temp = n;
        while (temp >= 10) {
            power *= 10;
            temp /= 10;
        }
        int result = 0;
        for( int j = n; j <= m; j += 1){
            temp = j;
            while(true){
                    temp = (temp / 10) + ((temp % 10) * power);
                    if (temp == j)
                        break;
                    if (temp > j && temp <= m)
                        result++;
                    }
            }
            cout << "Case #" << i << ": " << result << endl;
    }


    return 0;
}
