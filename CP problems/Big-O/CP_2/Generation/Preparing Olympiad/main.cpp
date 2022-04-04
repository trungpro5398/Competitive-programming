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

int main()
{
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    int n, l, r, x;
    cin >> n >> l >> r >> x;
    vector<int> c(n, 0);
    rep(i, 0, n)
    {
        cin >> c[i];
    }
    int ans = 0;
    rep(i, 0, (1 << n))
    {
        int sum = 0, cnt = 0;
        int minV = 1e9, maxV = -1e9;
        rep(j, 0, n)
        {
            if (i & (1 << j))
            {
                sum += c[j];
                cnt++;
                minV = min(minV, c[j]);
                maxV = max(maxV, c[j]);
            }
        }
        if (sum >= l && sum <= r && cnt >= 2 && maxV - minV >= x)
        {
            ans++;
        }
    }
    cout << ans;
}