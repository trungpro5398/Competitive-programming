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
const int N = (int)1e3;
int garden[N][N];
int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};
int m, n;
int cnt_dinh, cnt_canh;
void bfs(int si, int sj)
{
    garden[si][sj] = 2;
    queue<ii> q;
    q.push(mp(si, sj));
    while (!q.empty())
    {
        ii u = q.front();
        cnt_dinh++;
        q.pop();
        up(i, 0, 3)
        {
            int ni = u.fi + dr[i];
            int nj = u.se + dc[i];
            if (ni >= 1 && ni <= m && nj >= 1 && nj <= n)
            {
                if (garden[ni][nj] == 1)
                {
                    cnt_canh++;
                    garden[ni][nj] = 2;
                    q.push(mp(ni, nj));
                }
                else if (garden[ni][nj] == 2){
                    cnt_canh++;
                }
            }
        }
    }
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    cin >> m >> n;
    up(i, 1, m)
    {
        up(j, 1, n)
        {
            cin >> garden[i][j];
        }
    }
    ll ans = 0;
    up(i, 1, m)
    {
        up(j, 1, n)
        {
            if (garden[i][j] == 1)
            {
                cnt_dinh = 0;
                cnt_canh = 0;
                bfs(i, j);
                ans += 4 * cnt_dinh - cnt_canh;
            }
        }
    }
    cout << ans << endl;
}