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

void dfs(const vector<vector<int>> &dominos, vector<bool> &visited, vector<int> &order, int u)
{
    visited[u] = true;
    for (int v : dominos[u])
    {
        if (!visited[v])
            dfs(dominos, visited, order, v);
    }
    order.pb(u);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> dominos(n + 1);
        vector<bool> visited(n + 1, false);
        vector<int> topoSort;
        rep(i, 0, m)
        {
            int u, v;
            cin >> u >> v;
            dominos[u].pb(v);
        }
        up(i, 1, n)
        {
            if (!visited[i])
                dfs(dominos, visited, topoSort, i);
        }
        reverse(topoSort.begin(), topoSort.end());
        // Since it may not be a DAG, knock down the
        // dominos one by one and count the number.
        visited.assign(n + 1, false);
        int ans = 0;
        for (int i = 0; i < n; ++i)
        {
            int u = topoSort[i];
            if (!visited[u])
            {
                dfs(dominos, visited, topoSort, u);
                ++ans;
            }
        }
        cout << ans << endl;
    }
}