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
const int INF = 1e8;
vector<vector<int>> dist, path;
int floydWarshall(vector<vector<int>> &mat, int n)
{
    dist.resize(n + 1, vector<int>(n + 1));
    path.resize(n + 1, vector<int>(n + 1));
    up(i, 1, n)
    {
        up(j, 1, n)
        {
            dist[i][j] = i == j ? 0 : mat[i][j];
            if (i != j and dist[i][j] < INF)
                path[i][j] = i;
            else
                path[i][j] = -1;
        }
    }
    up(k, 1, n)
    {
        up(i, 1, n)
        {
            if (dist[i][k] > INF)
                continue;
            up(j, 1, n)
            {
                if (dist[k][i] < INF and dist[i][j] > dist[i][k] + dist[k][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    path[i][j] = path[k][j];
                }
            }
        }
    }
    // check negative cycle
    up(i, 1, n) if (dist[i][i] < 0) return false;
    return true;
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
}