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
map<char, int> m;

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int ans = 0;
        int cnt = 0;
        m.clear();
        rep(j, 0, s.size())
        {
            m.clear();
            cnt = 0;
            rep(i, j, s.size())
            {
                if (m[s[i]] == 0)
                {
                    cnt += 1;
                    m[s[i]] = 1;
                }
                else
                {
                    m.clear();
                    cnt = 1;
                    m[s[i]] = 1;
                }
                ans = max(ans, cnt);
            }
        }
        cout << ans << endl;
    }
}