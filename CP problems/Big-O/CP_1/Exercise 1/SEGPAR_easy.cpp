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
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    rep(i, 0, n) cin >> a[i];
    ll l = 0, r = 1e9, sav = r;
    while (l <= r)
    {
        ll mid = (l + r) / 2;
        ll cnt = 0, temp = 0;
        rep(i, 0, n)
        {
            if (temp + a[i] > mid)
            {
                temp = 0;
                cnt++;
            }
            temp += a[i];
        }
        
        if (cnt < k)
        {
            sav = mid;
            r = mid - 1;
        }
        else
            l = mid + 1;
    }
    cout << sav;
}