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
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int cnt = 0;
        vector<int> v;
        int dp[2] = {0};
        rep(i, 0, s.size())
        {
            if (s[i] == '0')
            {
                cnt += 1;
                dp[0] += 1;
            }
            else
            {
                v.pb(cnt);
                cnt = 0;
                dp[1] += 1;
            }
        }
        int ans = 0;
        int l = 0, r = s.size() - 1;
        int temp = dp[0], temp1 = dp[1];
        while (l < r and dp[1] <= dp[0])
        {
            if (s[l] == '1' and s[r] == '1')
            {
                l += 1;
                dp[1] -= 1;
            }
            else if (s[l] == '0')
            {
                l += 1;
                dp[0] -= 1;
            }
            else if (s[r] == '0')
            {
                r -= 1;
                dp[0] -= 1;
            }
            else
            {
                r -= 1;
                dp[1] -= 1;
            }
        }
        ans = max(ans, r - l + 1);
        l = 0, r = s.size() - 1;
        dp[0] = temp, dp[1] = temp1;
        while (l < r and dp[1] <= dp[0])
        {
            if (s[r] == '0')
                dp[0] -= 1;
            else
                dp[1] -= 1;
            r -= 1;
        }
        ans = max(ans, r - l + 1);
        l = 0, r = s.size() - 1;
        dp[0] = temp, dp[1] = temp1;

        while (l < r and dp[1] <= dp[0])
        {
            if (s[l] == '0')
                dp[0] -= 1;
            else
                dp[1] -= 1;
            l += 1;
        }
        ans = max(ans, r - l + 1);
        dp[0] = temp, dp[1] = temp1;

        while (l < r and dp[1] <= dp[0])
        {
            if (s[l] == '1' and s[r] == '1')
            {
                r -= 1;
                dp[1] -= 1;
            }
            else if (s[l] == '0')
            {
                l += 1;
                dp[0] -= 1;
            }
            else if (s[r] == '0')
            {
                r -= 1;
                dp[0] -= 1;
            }
            else
            {
                l += 1;
                dp[1] -= 1;
            }
        }
        ans = max(ans, r - l + 1);
        cout << ans << endl;
    }
}