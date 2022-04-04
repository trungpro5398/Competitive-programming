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
#define _io                           \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;
set<int> masks;

int main()
{

    int n, m;
    cin >> n >> m;
    ll total = 0;
    rep(i, 0, m)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        total += (1ll << a) + (1ll << b);
        masks.insert(total);
    }
    int res = 0;
    rep(i, 0, (1 << (n)))
    {
        bool ok = true;
        for (auto j : masks)
        {
            if (i & j == j)
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            res++;
        }
    }
    cout << res << endl;
}