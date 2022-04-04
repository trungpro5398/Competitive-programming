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
      ll n, l;
    cin >> n >> l;
    vector<double> a(n);
    up(i,0,n-1) cin >> a[i];
    sort(a.begin(), a.end());
    double ans = max(a[0], l - a[n-1]);
    rep(i,0,n){
        
        ans = max(ans, (a[i+1] - a[i]) / 2);
    }
    cout << fixed << setprecision(9) << ans;

}