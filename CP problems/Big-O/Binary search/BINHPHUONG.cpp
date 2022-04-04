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

bool check(ll k, ll x){
    ll cnt = 0;
    for(int i = 1; 1LL * i * i <= x; i++){
        cnt += (int) sqrt(x - 1LL*i*i);
    }
    return cnt >= k;
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    ll n;
    cin >> n;
    ll l = 2, r = 2e12, ans;
    while (l <= r)
    {
        ll mid = (l + r) >> 1;
        
        if (check(n,mid))
        {
            ans = mid;
            r = mid - 1;
        }
        else
            l = mid + 1;
    }
    cout << ans;
}