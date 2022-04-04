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
    while(t--){
        ll n, m;
        cin >> n >> m;
        vector<int> a;
        int cnt = 0;
        while( m ){
            if(m & 1 == 1){
                a.pb(cnt);
            }
            cnt += 1;
            m >>= 1;
        }
        reverse(a.begin(), a.end());
        rep(i,0,a.size()){
            if(i != a.size()-1){
                cout << "(" << n << "<<" << a[i] << ")" << " + " ;
            } 
            else{
                cout << "(" << n << "<<" << a[i] << ")" ;
            }
        }
        cout << endl;
    }
    
}