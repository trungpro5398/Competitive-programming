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
    int n, l, r;
    cin >> n >> l >> r;
    vector<pair<int, int>> a;
    up(i, 1, n)
    {
        int x, y;
        cin >> x >> y;
        a.pb(mp(x, y));
    }
    sort(a.begin(), a.end(), [](ii a, ii b)
         { return a.fi < b.fi; });
    int ans = 0, r1 = 0;
    rep(i, 0, a.size())
    {
        if (a[i].fi < r1 or (a[i].fi < l or a[i].se > r))
        {
            ans = max(ans, a[i].se - a[i].fi);
             
        }
        r1 = max(r1, a[i].se);
    }
    cout << ans;
}