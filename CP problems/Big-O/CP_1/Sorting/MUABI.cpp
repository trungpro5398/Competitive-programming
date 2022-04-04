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
struct muabi {
    int a;
    int b;

    bool operator < (const muabi &p) const {
      
        return b > p.b;
    }
};
int main(){

    int n, m;
    cin >> n >> m;
    vector<muabi> x;
    rep(i,0,m){
        int a,b;
        cin >> a >> b;
        x.pb(muabi({a,b}));
    }
    sort(x.begin(), x.end());
    
    ll ans = 0;
    int l = 0;
    while(n && l < x.size()) {
        if( x[l].a >= n )
        {   
            ans += n * x[l].b;
            break;
        }
        ans += x[l].a * x[l].b;
        n -= x[l].a;
        l += 1;
    }
    cout << ans << endl;
}