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
const int mxN = 1e3 + 5;
int a[mxN];
vector<int> graph[mxN];
bool visited[mxN];
vector<int> result;
vector<int> dist;
void topo(int u)
{
    visited[u] = true;
    for (int v : graph[u])
    {
        if (visited[v] == false)
            topo(v);
    }
    result.push_back(u);
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    map<int, int> mp;
    up(i, 1, n)
    {
        cin >> a[i];
        mp[a[i]] = i;
    }
    sort(a + 1, a + n + 1);
    memset(visited, false, sizeof(visited));
    for (int i = 1; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            int s = a[i] + a[j];
            int idx = lower_bound(a, a + n + 1, s) - a;
            if (a[idx] == s)
            {
                graph[mp[a[i]]].push_back(mp[s]);
                graph[mp[a[j]]].push_back(mp[s]);
            }
        }
    }
    for (int i = 1; i <= n; i++)
    {
        if (visited[i] == false)
            topo(i);
    }
    dist.assign(n + 1, 1);
    for (int i = result.size() - 1; i >= 0; i--)
    {
        int u = result[i];
        for (int v : graph[u])
        {
            dist[v] = max(dist[v], dist[u] + 1);
        }
    }
    int ret = dist[1];
    for (int i = 2; i <= n; i++)
    {
        ret = max(ret, dist[i]);
    }
    cout << ret << '\n';
}