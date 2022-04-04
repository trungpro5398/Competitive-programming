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
vector<int> graph[MAX];
int low[MAX], num[MAX];
bool isCut[MAX];
vector<ii> bridges;
int n, m;
int counter;

void dfs(int u, int p)
{
    counter++;
    num[u] = low[u] = counter;
    int numChild = 0;

    for (int v : graph[u])
    {
        if (v == p)
            continue;
        if (num[v] > 0)
            low[u] = min(low[u], num[v]);
        else
        {
            dfs(v, u);
            low[u] = min(low[u], low[v]);
            numChild++;
            if (low[v] > num[u])
                bridges.pb(mp(u, v));
            if (low[v] >= num[u] and p != -1)
                isCut[u] = true;
        }

    }

    if (p == -1 and numChild > 1)
        isCut[u] = true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    for (int u, v, i = 0; i < m; i++)
    {
        cin >> u >> v;
        graph[u].pb(v);
        graph[v].pb(u);
    }

    up(i, 1, n)
    {
        if (num[i] == 0)
            dfs(i, -1);
    }
    cout << "Bridges:\n";
    for (ii bridge : bridges)
        cout << bridge.fi << " " << bridge.se << "\n";
    cout << "Cut vertices:\n";
    up(i, 1, n)
    {
        if (isCut[i])
            cout << " " << i;
    }
    cout << "\n";
    return 0;
}