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
int n, m;
int counter;
map<string, int> m1;
map<int, string> m2;
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

        do
        {
            v = st.top();
            if (v !=u)
                cout << m2[v] << ", ";
            else
                cout << m2[v];
            st.pop();
            found[v] = true;
        } while (v != u);
        cout << endl;
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
    int t = 1;
    while (cin >> n >> m)
    {
        m1.clear();
        m2.clear();
        up(i, 1, n)
        {
            graph[i].clear();
        }
        if (n == 0 and m == 0)
            break;
        string a, b;
        int cnt = 0;
        rep(i, 0, m)
        {
            cin >> a >> b;
            if (!m1[a] and !m1[b])
            {
                m1[a] = ++cnt;
                m2[cnt] = a;
                m1[b] = ++cnt;
                m2[cnt] = b;
                graph[m1[a]].pb(m1[b]);
            }
            else if (!m1[a])
            {
                m1[a] = ++cnt;
                m2[cnt] = a;
                graph[m1[a]].pb(m1[b]);
            }
            else if (!m1[b])
            {
                m1[b] = ++cnt;
                m2[cnt] = b;
                graph[m1[a]].pb(m1[b]);
            }
            else
            {
                graph[m1[a]].pb(m1[b]);
            }
        }
        cout << "Calling circles for data set " << t << ":" << endl;

        tarjan();
        t++;
        cout << endl;
    }
}