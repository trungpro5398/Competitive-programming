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

int n, ans;
vector<int> v[15];

int backtracking(int u, vector<int> &vis, int ans1, int cnt)
{
    if (cnt > n + 1 or (u == 0 and cnt != 1 and cnt != n + 1) or ans1 > ans)
        return 1e9;
    if (cnt == n + 1 and u == 0)
    {
        return min(ans, ans1);
    }

    for (int i = 0; i < v[u].size(); i++)
    {
        if (i == u)
            continue;
        int e = v[u][i];
        if (i == 0 or !vis[i])
        {
            vis[i] = 1;
            ans = min(ans, backtracking(i, vis, ans1 + e, cnt + 1));
            vis[i] = 0;
        }
    }
    return ans;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    rep(i, 0, n)
    {
        rep(j, 0, n)
        {
            int x;
            cin >> x;

            v[i].pb(x);
        }
    }
    vector<int> vis(n, 0);
    ans = 1e9;
    ans = min(ans, backtracking(0, vis, 0, 1));
    cout << ans << endl;
}