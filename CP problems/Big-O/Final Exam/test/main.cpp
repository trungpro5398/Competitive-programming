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
typedef pair<int,int> ii;
int main()
{
    int t, n;
    cin >> t;
    while( t ){
        t -= 1;
        cin >> n;
        ll a[n];
        rep(i,0,n)
        cin >> a[i];
        ll res = 0;
        rep(i,3,n+1){
            rep(j,0, n-i+1){
                ll temp = 0;
                rep(k, j+1, j+i-1){
                    temp = max(temp,(a[j] - a[k]) * (a[k] - a[j+i-1]));
                }
                res += temp;
            }
        }
        cout << res <<endl;
    }
    return 0;
}
