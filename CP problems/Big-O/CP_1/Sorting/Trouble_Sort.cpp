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
int a[(100000 + 1) / 2], b[100000 / 2];

int& get(int i) {
  return (i % 2 ? b : a)[i / 2];
}
int main(){
    
    int t;
    cin >> t;
    up(t1,1,t){
        int n;
        cin >> n;
       

        rep(i,0,n){
            cin >> get(i);
            
        }
        sort(a, a + (n+1)/2);
        sort(b, b + n/2);

        int ans = -1;
        rep(i,1,n){
            if(get(i-1)> get(i)){
                ans = i-1;
                break;
            }
        }
        cout << "Case #" << t1 << ": ";
        if(ans == -1)
            cout << "OK" << endl;
        else
            cout << ans << endl;
    }
}