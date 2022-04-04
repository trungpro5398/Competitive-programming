#include <bits/stdc++.h>

#define bug(x) cout << #x << " = " << x << endl;
#define fr(a) freopen(a,"r",stdin);
#define fw(a) freopen(a,"w",stdout);
#define tc() int tc;cin >> tc; for (int _tc=1;_tc<=tc;_tc++)
#define up(i,l,r) for (int i=l;i<=r;i++)
#define down(i,r,l) for (int i=r;i>=l;i--)
#define rep(i,l,r) for (int i=l;i<r;i++)
#define pb push_back
#define mp make_pair
#define ins insert
#define fi first
#define se second
#define v2d(i) vector<vector<i>>;
#define v1d(i) vector<i>;
#define map_1(i,j) map<i,j>;
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll,ll> ii;

int main(){

    ll n, l;
    cin >> n >> l;
    vector<double> a(n);
    up(i,0,n-1) cin >> a[i];
    sort(a.begin(), a.end());
    double ans = max(a[0], l - a[n-1]);
    rep(i,0,n){
        
        ans = max(ans, (a[i+1] - a[i]) / 2);
    }
    cout << fixed << setprecision(2) << ans;
}