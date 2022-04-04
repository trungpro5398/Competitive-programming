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
    int n, m;
    cin >> n >> m;
    int a[n][m];
    ll ans = 0;
    int ind[n];
    rep(i, 0, n)
    {
        rep(j, 0, m)
        {
            cin >> a[i][j];
        }
        ans ^= a[i][0];
        ind[i] = 0;
    }
    bool flag = false;
    
    if (ans == 0)
    {
        rep(i, 0, n)
        {
            rep(j, 0, m)
            {
                if (a[i][j] != a[i][0])
                {
                    flag = true;
                    ind[i] = j;
                    break;
                }
            }
            if (flag)
                break;
        }
    }
    else
        flag = true;

    if (flag)
    {
        cout << "TAK" << endl;
        for (int x : ind)
        {
            cout << x + 1 << ' ';
        }
    }
    else
    {
        cout << "NIE" << endl;
    }
}