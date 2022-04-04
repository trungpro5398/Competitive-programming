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

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    vector<vector<int>> vis(401, vector<int>(401, 0));
    rep(i, 0, n)
    {
        int a, b, c;
        cin >> a >> b >> c;
        vis[a + 200][b + 200] = 1 << (c - 1);
    }
    ll ans = 0;
    up(i, 0, 400)
    {
        up(j, 0, i)
        {
            vector<ll> f(16, 0);
            up(k, 0, 400)
            {
                if (vis[i][k] and vis[j][k] and vis[i][k] != vis[j][k])
                {
                    int temp = vis[i][k] | vis[j][k];
                    ans += f[15 - temp];
                    f[temp]++;
                }
            }
        }
    }
    cout << ans;
}