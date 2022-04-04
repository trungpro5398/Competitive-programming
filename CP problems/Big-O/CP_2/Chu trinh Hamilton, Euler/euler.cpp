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
const int Max = 110;
int deg[Max][Max];
int n, m;
vector<int> result;
void findEulerPath(int u)
{
    rep(v, 0, n)
    {
        if (deg[u][v] > 0)
        {
            deg[u][v]--;
            deg[v][u]--;
            findEulerPath(v);
        }
    }
    result.pb(u);
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n >> m;
    for (int u, v, i = 0; i < m; i++)
    {
        cin >> u >> v;
        deg[u][v]++;
        deg[v][u]++;
    }
    int u = -1, v = -1;
    bool isConnected = true, bad = false;
    rep(i, 0, n)
    {
        int cnt = 0;
        rep(j, 0, n)
        {
            cnt += deg[i][j];
        }
        if (cnt == 0)
            isConnected = false;
        if (cnt % 2 == 1)
        {
            if (u == -1)
                u = i else if (v == -1)
                    v = i;
            else
            {
                bad = true;
                break;
            }
        }
    }
    if (bad)
    {
        cout << "Graph does not euler path" << endl;
        return 0;
    }
    if (u != -1)
    {
        deg[u][v] = deg[v][u] = 1;
        m++;
    }
    findEulerPath(0);
    if (!isConnected or result.size() != m + 1)
    {
        cout << "Graph is disconnected" << endl;
        return 0;
    }
    if (u == -1)
    {
        cout << "Euler cycle: ";
        for (int v : result)
        {
            cout << v << " ";
        }
        return 0;
    }
    
}