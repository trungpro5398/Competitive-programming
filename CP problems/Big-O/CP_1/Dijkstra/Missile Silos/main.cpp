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

const int maxN = 1e5 + 100;
const int INF = 1e9;

vector<int> dist;
vector<ii> adj[maxN];
int u[maxN], v[maxN], w[maxN];
int n, m, s, l, res;
void calcNumberLocated(int u, int v, int w)
{
    if (dist[u] < l && dist[v] < l && 2 * l == dist[u] + dist[v] + w)
    {
        res++;
        return;
    }
    if (dist[u] < l && dist[u] + w > l && dist[u] + dist[v] + w > 2 * l)
        res++;
    if (dist[v] < l && dist[v] + w > l && dist[u] + dist[v] + w > 2 * l)
        res++;
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    cin >> n >> m >> s;
    rep(i, 0, m)
    {
        cin >> u[i] >> v[i] >> w[i];
        adj[u[i]].pb(mp(v[i], w[i]));
        adj[v[i]].pb(mp(u[i], w[i]));
    }
    dist.resize(n + 1, INF);
    priority_queue<ii, vector<ii>, greater<ii>> pq;
    dist[s] = 0;
    pq.push(mp(0, s));
    while (!pq.empty())
    {
        ii cur = pq.top();
        pq.pop();
        int u = cur.se;
        if (dist[u] < cur.fi)
            continue;
        for (auto it : adj[u])
        {
            int v = it.fi;
            int w = it.se;
            if (dist[v] > dist[u] + w)
            {
                dist[v] = dist[u] + w;
                pq.push(mp(dist[v], v));
            }
        }
    }
    cin >> l;
    up(i, 1, n)
    {
        if (dist[i] == l)
            res++;
    }
    rep(i, 0, m)
    {
        calcNumberLocated(u[i], v[i], w[i]);
    }
    cout << res << endl;
}