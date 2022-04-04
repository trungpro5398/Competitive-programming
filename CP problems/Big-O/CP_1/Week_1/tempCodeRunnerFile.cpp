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
map < ll, ii> vis;
int main(){
    
    int t;
    cin >> t;
    up(t1,1,t){

        ll R, k, N;
        cin >> R >> k >> N;
        ll a[N];
        
        rep(i,0,N){
            cin >> a[i];
        }
        ll res = 0, cnt = 0, i = 0;
        while(cnt < R){
            vis[i] = make_pair(cnt, res);
            ll steps, euro;
            steps = 0, euro = 0;
            while(steps < N && euro + a[i] <=k){
                euro += a[i];
                steps++;
                i = ( i + 1 ) % N;
            }
            res += euro;
            cnt += 1;
            if(vis.find(i) != vis.end()){
                ll temp_res = res - vis[i].se;
                ll len_i = cnt - vis[i].fi;
                R -= vis[i].fi;
                ll times = R / len_i;
                R %= len_i;
                res = temp_res * times + vis[i].se;
                cnt = 0;
                vis.clear();
            }
        }
        cout << "Case #" << t1 << ": " << res << endl; 
    }
}