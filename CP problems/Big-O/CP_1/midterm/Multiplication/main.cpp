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

ll cv(int n)
{
    ll res = n;
    while (res >= 10)
    {
        ll temp = res;
        res = 0;
        while (temp)
        {
            res += temp % 10;
            temp /= 10;
        }
    }
    return res;
}

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    while (t--)
    {
        ll n, m;
        cin >> n >> m;
        ll ans = 1;
        n = cv(n);
        while (m and n != 1)
        {
            ans *= cv(n);
            n++;
            m--;
        }
        ans = cv(ans);
        ll sav = m / 10;
        ll sav1 = m % 10;
        ll temp = 1;
        up(i, 1, 9)
        {
            temp *= i;
        }
        temp = cv(temp);
        if (sav > 0)
            ans *= temp * sav;
        up(i, 1, sav1)
        {
            ans *= i;
        }
        ans = cv(ans);
        cout << ans << endl;
    }
}