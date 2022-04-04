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
const int maxn = (int)3e5 + 3;
const int maxa = (1 << 20) + 3;

int a[maxn];
int cnt[2][maxa];
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    ll ans = 0;
    rep(i, 0, n)
    {
        cin >> a[i];
    }
    int x = 0;
    cnt[1][0] = 1; // if index 1 got zero => increase 1
    // cnt[0][a[0]] = 1; // if index 2 got a[0] => increase 1 
    rep(i, 0, n)
    {
        x ^= a[i];
        ans += cnt[i % 2][x];
        ++cnt[i % 2][x];
    }
    cout << ans;
}