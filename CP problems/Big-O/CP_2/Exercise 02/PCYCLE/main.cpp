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
const int Max = 201;
vector<int> graph[Max];

int n, m, c[Max][Max];
vector<int> res;
int vis[Max];
bool br;
void dfs(int u, int cnt, int pow)
{
    if (u == 1 and cnt == m + 1 and pow >= 0)
    {
        br = true;
        return;
    }
    if (br)
        return;
    if (pow < 0)
    {
        return;
    }
    for (auto v : graph[u])
    {
        if (br)
            return;
        if (vis[v] == 0 or v == 1)
        {
            vis[v] = 1;
            res.push_back(v);
            dfs(v, cnt + 1, pow + c[u][v]);
            if (br)
                return;
            vis[v] = 0;
            res.pop_back();
        }
    }
}
int main()
{
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    cin >> n >> m;
    for (int u, v, w, i = 0; i < m; i++)
    {
        cin >> u >> v >> w;
        graph[u].pb(v);
        graph[v].pb(u);
        c[u][v] = w;
    }
    up(i, 1, n)
    {
        memset(vis, 0, sizeof(vis));
        br = false;
        res.clear();
        res.pb(i);
        dfs(i, 1, 0);
        if (res.size() == m + 1)
        {
            for (auto x : res)
                cout << x << " ";
            return 0;
        }
    }
    cout << -1;
}