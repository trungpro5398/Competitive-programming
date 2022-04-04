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
vector<vector<int>> adj;
vector<int> indegree, order;
int Missing;

bool kahn()
{
    queue<int> q;
    up(i, 1, n)
    {
        if (indegree[i] == 0)
        {
            q.push(i);
        }
    }
    Missing = false;
    while(!q.empty()){
        if(q.size() > 1){
            Missing = true;
        }
        int u = q.front();
        q.pop();
        order.pb(u);
        for(auto v: adj[u]){
            indegree[v] --;
            if(!indegree[v]){
                q.push(v);
            }
        }
    }
    return order.size() == n;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        cin >> n >> m;
        adj.assign(n + 1, vector<int>());
        indegree.assign(n + 1, 0);
        order.assign(n + 1, 0);
        order.clear();
        for (int u, v, i = 0; i < m; i++)
        {
            cin >> u >> v;
            adj[u].pb(v);
            indegree[v]++;
        }
        if(!kahn()){
            cout << "recheck hints" << endl;
        }else if(Missing == true){
            cout << "missing hints" << endl;
        }else{
            for(int x : order){
                cout << x << ' ';
            }
            cout << endl;
        }
    }
}