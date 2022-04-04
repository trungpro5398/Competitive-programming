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
map<int, int> m;

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int tc;
    cin >> tc;
    while (tc--)
    {
        int n;
        cin >> n;
        vector<int> v(n);
        for (auto &i : v)
        {
            cin >> i;
        }
        vector<int> v1((n+1) * (n+1), 0);
        ll ans = 0;
        down(i, n - 1, 0)
        {
            int j = i + 1;
            rep(k, j + 1, n)
            {
                v1[v[j] * n + v[k]]++;
            }
            rep(k, 0, i)
            {
                ans += v1[v[k] * n + v[i]];
            }
        }
        cout << ans << endl;
    }
}