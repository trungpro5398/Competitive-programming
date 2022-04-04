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
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll,ll> ii;

bool check(ll mid, ll R, ll B, vector<ll> &m, vector<ll> &s, vector<ll> &p){
    vector<ll> c(m.size());
    rep(i,0,c.size()){
        c[i] = max(1LL * 0, min(m[i], (ll) (mid-p[i]) / s[i]));
    }
    sort(c.begin(), c.end(), [](ll a, ll b){return a > b;});
    ll ans = 0;
    rep(i,0, R){
        ans += c[i];
    }
    return ans >= B;
}
ll solve(){
    ll R, B, C;
    cin >> R >> B >> C;
    vector<ll> m(C), s(C), p(C);
    rep(i,0,C){
        cin >> m[i] >> s[i] >> p[i];
    }
    ll l = 0, r = 1e9, ans = 1e9;
    while(l <= r){
        ll mid = (l+r)/2;
        if(check(mid, R, B, m, s, p)){
            ans = mid;
            r = mid - 1;
        }
        else{
            l = mid + 1;
        }
    }
    return ans;
}
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    up(tc, 1, t)
    {
        cout << "Case #" << tc << ": " << solve() << endl;
    }
}