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

int main(){
    int t;
    cin >> t;
    up(t1,1,t){
        ll n, k, v;
        cin >> n >> k >> v;
        string s[n];
        rep(i,0,n) cin >> s[i];
        v = (v - 1) % (n * k);
        int cnt = 0;
        while(v--){
            cnt = ( cnt + k ) % n;
        }
        cout << "Case #" << t1 << ":";
        rep(i,0, k - (n - cnt)) cout << " " << s[i];
        rep(i,cnt, min(n, cnt + k)) cout << " " << s[i];
        cout << endl;
    }
    
}