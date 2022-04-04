#include <bits/stdc++.h>

#define bug(x) cout << #x << " = " << x << endl;
#define fr(a) freopen(a, "r", stdin);
#define fw(a) freopen(a, "w", stdout);
// #define tc()   \
//     int tc;    \
//     cin >> tc; \
//     for (int _tc = 1; _tc <= tc; _tc++)
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

ll r1, t;
bool check(ll x)
{
    // 2 vòng đen trắng, cho nên cần cộng thêm 1
    bool k =  ((x + 1) * (2 * r1 + 2 * x + 1) > t);
    return k;
}

ll solve(){
    cin >> r1 >> t;
    ll l = 0, r = ((1LL * (1e18 / r1) <= 1LL * 1e9) ? 1LL * (1e18 / r1) : 1LL * 1e9), ans = r;
    while (l <= r){
        ll mid = (l + r) / 2;
        if (check(mid)){
            ans = mid;
            r = mid - 1;
        }
        else
            l = mid + 1;
    }
    return ans;
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    up(tc, 1, t)
    {
        cout << "Case #" << tc << ": " << solve() << endl;
    }
}