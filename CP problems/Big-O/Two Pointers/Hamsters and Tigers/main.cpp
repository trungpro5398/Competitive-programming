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
    string s;
    cin >> n >> s;
    int cnt = 0;
    rep(i, 0, n)
    {
        if (s[i] == 'T')
        {
            cnt++;
        }
    }
    int cnt1 = 0, ans = (1 << 28);
    rep(i, 0, n)
    {
        int cnt1 = 0;
        rep(j, i, i + cnt)
        {
            int k = j % n;
            if (s[k] == 'T')
            {
                cnt1++;
            }
        }
        ans = min(ans, (cnt - cnt1));
    }
    cout << ans;
}