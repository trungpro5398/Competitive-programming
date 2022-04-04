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
    int tc;
    cin >> tc;
    up(t, 1, tc)
    {
        int S, p, N;
        cin >> N >> S >> p;
        int high = (p - 1) * 3;
        int low = high - 1;
        high = max(high, 0);
        low = max(low, 0);
        int res = 0;
        rep(i, 0, N)
        {
            int x;
            cin >> x;
            if (p == 0)
            {
                res++;
            }
            else if (x == 0)
                continue;
            else if (x > high)
            {
                res++;
            }
            else if (S > 0 and x >= low)
            {
                res++;
                S -= 1;
            }
        }
        cout << "Case #" << t << ": " << res << "\n";
    }
}