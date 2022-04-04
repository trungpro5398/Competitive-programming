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
vector<int> cost, minCost;
vector<int> componentId;
int n, m;
int counter;
int numScc;
int cnt[MAX];
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
        numScc++;
        int v;
        do
        {
            v = st.top();
            st.pop();
            componentId[v] = numScc;
            found[v] = true;
        } while (v != u);
        cout << "\n";
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
    cin >> n;
    rep(i, 0, n)
    {
        int x;
        cin >> x;
        cost.pb(x);
    }
    cin >> m;
    for (int u, v, i = 0; i < m; i++)
    {
        cin >> u >> v;
        graph[u].pb(v);
    }
    tarjan();
    minCost.assign(numScc, 1e9 + 8);
    up(i, 1, n)
    {
        int v = componentId[i];
        int c = cost[i - 1];
        if (minCost[v] > c)
            minCost[v] = c, cnt[v] = 1;
        else if (minCost[v] == c)
            cnt[v]++;
    }

    ll a = 0, b = 1;
    up(i,1,n){
        a += minCost[i];
        b *= cnt[i];
        b % 1000000007;
    }
    cout << a << " " << b;
    return 0;
}