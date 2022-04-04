#include <bits/stdc++.h>

#define bug(x) cout << #x << " = " << x << endl;
#define fr(a) freopen(a,"r",stdin);
#define fw(a) freopen(a,"w",stdout);
#define tc() int tc;cin >> tc; for (int _tc=1;_tc<=tc;_tc++)
#define up(i,l,r) for (int i=l;i<=r;i++)
#define down(i,r,l) for (int i=r;i>=l;i--)
#define rep(i,l,r) for (int i=l;i<r;i++)
#define pb push_back
#define mp make_pair
#define ins insert
#define fi first
#define se second
typedef long long int ll;
typedef unsigned long long int llu;


using namespace std;
const int N = 1005;

int f[N][N], c[N][N], k, n, m;
char a[N], b[N];
int main()
{
    while (scanf("%d", &k), k) {
        scanf("%s%s", a + 1, b + 1);
        n = strlen(a + 1);
        m = strlen(b + 1);
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (a[i] == b[j])
                    c[i][j] = c[i - 1][j - 1] + 1;
                else
                    c[i][j] = 0;
                f[i][j] = max(f[i - 1][j], f[i][j - 1]);
                for (int e = k; e <= c[i][j]; ++e)
                    f[i][j] = max(f[i][j], f[i - e][j - e] + e);
            }
        }
        printf("%d\n", f[n][m]);
    }
}
