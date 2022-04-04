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
vector<int> low, num;
vector<bool> found;
stack<int> st;
vector<int> componentId;
int n, m;
int counter;
int numScc;
void dfs(int u)
{
    counter++;
    num[u] = low[u] = counter;
    st.push(u);
    for (int v : graph[u])
    {
        if (!found[v])
        {
            if (num[v] > 0)
                low[u] = min(low[u], num[v]);
            else
            {
                dfs(v);
                low[u] = min(low[u], low[v]);
            }
        }
    }
    if (low[u] == num[u])
    {

        int v;
        numScc++;
        while(1){
            int top = st.top(); st.pop();
            componentId[top] = numScc; // assign SCC idx to vertex
            found[top] = false;
            if(u == top) break;
        }
    }
}

void tarjan()
{
    counter = 0;
    low.assign(n + 1, 0);
    num.assign(n + 1, 0);
    found.assign(n + 1, false);
    counter = 0;
    st = stack<int>();
    up(i, 1, n)
    {
        if (num[i] == 0)
            dfs(i);
    }
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
        numScc = 0;
        counter = 0;
        graph[MAX].assign(n + 1, 0);
        low.assign(n + 1, 0);
        num.assign(n + 1, 0);
        found.assign(n + 1, false);
        componentId.assign(n+1, -1);
        cin >> n >> m;
        for (int u, v, i = 0; i < m; i++)
        {
            cin >> u >> v;
            graph[u].pb(v);
        }
        tarjan();
        // count indegree of each SCC
        vector<int> componentIndegree(numScc+1, 0);
        for (int i = 1; i <= n; i++)
            for (auto &neigh : graph[i])
            {
                // not within the same strongly connected component
                if (componentId[neigh] != componentId[i])
                    componentIndegree[componentId[neigh]]++;
            }
        int res = count(componentIndegree.begin(), componentIndegree.end(), 0);
        cout << res << endl;
    }
    return 0;
}