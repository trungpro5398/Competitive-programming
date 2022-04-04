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
    while (t--)
    {
        ll n, m;
        cin >> n >> m;
        ll ans = n;
        ll temp;
        while (ans >= 10)
        {
            temp = ans;
            ans = 0;
            while (temp)
            {
                ans += temp % 10;
                temp /= 10;
            }
        }
        cout << ans << endl;
        rep(i, 1, m)
        {
            n += 1;
            temp = n * ans;
            while (temp)
            {
                ans += temp % 10;
                temp /= 10;
            }
            while (ans >= 10)
            {
                temp = ans;
                ans = 0;
                while (temp)
                {
                    ans += temp % 10;
                    temp /= 10;
                }
            }
            cout << ans << endl;
        }

        cout << ans << endl;
    }
}