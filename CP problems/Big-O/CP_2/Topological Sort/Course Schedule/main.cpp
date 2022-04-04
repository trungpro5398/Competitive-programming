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

vector<int> topoSort(vector<vector<int>> &adj, vector<int> &indegree)
{
    int n = indegree.size();
    priority_queue<int, vector<int>, greater<int>> zero_indegree;
    vector<int> topoSorted;
    // vector<bool> avail(n, true);

    for (int i = 0; i < indegree.size(); i++)
        if (indegree[i] == 0)
        {
            zero_indegree.push(i);
            // avail[i] = false;
        }

    while (!zero_indegree.empty())
    {
        int u = zero_indegree.top();
        zero_indegree.pop();

        topoSorted.push_back(u);

        for (int i = 0; i < adj[u].size(); i++)
        {
            int v = adj[u][i];
            indegree[v]--;
            if (indegree[v] == 0)
            {
                zero_indegree.push(v);
            }
        }
    }

    return topoSorted;
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj;
    vector<int> indegree;
    adj.resize(n);
    indegree.assign(n, 0);
    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u - 1].push_back(v - 1);
        indegree[v - 1]++;
    }
    vector<int> res = topoSort(adj, indegree);
    if (res.size() < n)
    {
        cout << "IMPOSSIBLE" << endl;
        return 0;
    }
    for (int i : res)
    {
        cout << i + 1 << " ";
    }
}