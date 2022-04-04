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
const int MAX = 1e5 + 10;

int n, m;
vector<int> graph[MAX];
int indegree[MAX];
int dist[MAX];
int path[MAX];

void printPath(int u)
{
    if (u == 0)
        return;
    printPath(path[u]);
    cout << u << " ";
}

void bfs()
{
    queue<int> q;
    for (int i = 1; i <= n; i++)
    {
        if (indegree[i] == 0)
        {
            q.push(i);
        }
    }
    vector<int> order;
    int u, v;
    while(!q.empty()){
        u = q.front();
        q.pop();
        order.pb(u);
        for(auto v: graph[u]){
            indegree[v] --;
            if(!indegree[v]){
                q.push(v);
            }
        }
    }
    if (order.size() < n) {
        cout << "Not a DAG";
        exit(0);
    }
    dist[1] = 1;
    for(auto u: order){
        if(dist[u] > 0){
            for(auto v: graph[u]){
                if(dist[v] < dist[u] + 1){
                    dist[v] = dist[u] + 1;
                    path[v] = u;
                }
            }
        }
    }

}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    assert(2 <= n && n <= 100000);
    assert(1 <= m && m <= 200000);

    for (int u, v, i = 0; i < m; i++)
    {
        cin >> u >> v;
        assert(1 <= u && u <= n);
        assert(1 <= v && v <= n);
        graph[u].pb(v);
        indegree[v]++;
    }
    bfs();
    if (!dist[n]) {
        cout << "IMPOSSIBLE";
        return 0;
    }
    cout << dist[n] << "\n";
    printPath(n);
}