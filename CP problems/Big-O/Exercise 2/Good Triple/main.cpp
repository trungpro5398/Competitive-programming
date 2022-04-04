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

string s;
bool check(int l, int r)
{
    rep(i, l, r)
    {
        for (int j = 1; i + 2 * j < r; j++)
        {
            if (s[i] == s[i + j] and s[i + j] == s[i + 2 * j])
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);

    cin >> s;
    ll n = s.size();
    ll ans = n * (n + 1) / 2;
    rep(i, 0, n)
    {
        rep(j, i, n)
        {
            if (j - i == 9)
                break;
            if (!check(i, j + 1))
            {
                ans -= 1;
            }
        }
    }
    cout << ans;
}