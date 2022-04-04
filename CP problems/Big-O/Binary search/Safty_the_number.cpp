#include <bits/stdc++.h>

#define bug(x) cout << #x << " = " << x << endl;
#define fr(a) freopen(a, "r", stdin);
#define fw(a) freopen(a, "w", stdout);
#define tc()   \
    int tc;    \
    cin >> tc; \
    for (int _tc = 1; _tc <= tc; _tc++)
#define up(i, l, r) for (int i = l; i <= r; i++)
#define down(i, r, l) for (int i = r; i >= l; i--)
#define rep(i, l, r) for (int i = l; i < r; i++)
#define pb push_back
#define mp make_pair
#define ins insert
#define fi first
#define se second
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    up(tc, 1, t)
    {
        cout << "Case #" << tc << ": ";
        int n;
        cin >> n;
        double a[n];
        double sum = 0;
        up(i, 0, n - 1)
        {
            cin >> a[i];
            sum += a[i];
        }
        double ans = 0, l = 0, r = sum;
        while(r - l > 1e-10)
        {
            double mid = (l + r) / 2;
            ans = 0.0;
            rep(i,0,n){
                
                ans += max(0.0, (mid - a[i]));
            }
        
            if(ans >= sum)
                r = mid;
            else
                l = mid;
        }
        rep(i,0,n)
        {
            double temp = (r - a[i]) * 100 / sum;
            cout << fixed << setprecision(6) <<  max(0.0, temp) << " ";
        }
        cout << endl;
    }
}