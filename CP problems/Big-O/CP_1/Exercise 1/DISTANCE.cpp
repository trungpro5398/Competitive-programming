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
int a[27], b[27];
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    string s, t;
    cin >> s >> t;
    for(auto &i : s)
        a[int(i-'a')]++;
    for(auto &i : t)
        b[int(i-'a')]++;
    int ans = 0;
    rep(i,0,26)
        ans += max(a[i],b[i]) - min(a[i],b[i]);
    cout << ans;
    
}