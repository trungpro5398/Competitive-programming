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
const int N = 1000 + 1;
int n, m;
vector<int> adj[N];
int edge_count[N][N];
int vis[N];
int parent[N];
bool exists_cycle;
int v_back;

void dfs(int u)
{
    vis[u] = 1;
    for (int &v : adj[u])
    {
        if (edge_count[u][v] == 0 || vis[v] == 2)
            continue;
        parent[v] = u;
        if (vis[v] == 1)
        {
            exists_cycle = true;
            v_back = v;
            break;
        }
        dfs(v);
        if (exists_cycle)
            break;
    }
    vis[u] = 2;
}

bool isCycle()
{
    fill(vis, vis + n + 1, 0);
    exists_cycle = false;
    up(i, 1, n)
    {
        if (!vis[i])
        {
            dfs(i);
            if (exists_cycle)
                break;
        }
    }
    return exists_cycle;
}

vector<ii> getEdges()
{
    vector<ii> edges;
    int v = v_back;
    do
    {
        edges.pb(mp(parent[v], v));
        v = parent[v];
    } while (v != v_back);
    return edges;
}

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    cin >> n >> m;
    rep(i, 0, m)
    {
        int x, y;
        cin >> x >> y;
        if (edge_count[x][y] == 0)
        {
            adj[x].pb(y);
        }
        edge_count[x][y]++;
    }

    if (!isCycle())
    {
        cout << -1;
        return 0;
    }
    vector<ii> edges = getEdges();
    vector<ii> ans;
    for (ii &e : edges)
    {
        if (edge_count[e.fi][e.se] > 1)
        {
            continue;
        }
        int tmp = edge_count[e.fi][e.se];
        edge_count[e.fi][e.se] = 0;
        if (!isCycle())
        {
            ans.pb(e);
        }
        edge_count[e.fi][e.se] = tmp;
    }
    if (ans.size() == 0)
    {
        cout << -1;
    }
    else
    {
        cout << ans.size() << endl;
        sort(ans.begin(), ans.end(), [](ii a, ii b)
             {
            if(a.fi==b.fi)
                return a.se<b.se;
             return a.fi < b.fi; });

        for (ii &e : ans)
        {
            cout << e.fi << " " << e.se << endl;
        }
    }
}