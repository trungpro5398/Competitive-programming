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

    int n;
    cin >> n;
    int a[n];
    int zero[n] = {0};
    int dp[n] = {0};
    up(i,0,n-1){
        cin >> a[i];
        
    }
    int q;
    cin >> q;
    
    rep(i, 0, n){
        if( i == 0 ){
            dp[i] = a[i];
            zero[i] = a[i] ^ 1;
        }
        else{
            dp[i] ^= dp[i-1] ^ a[i];
            zero[i] = zero[i-1] + (a[i] ^ 1);
        }
    }
    up(i,0,q-1){
        int l,r;
        cin >> l >> r;
        l -= 1;
        r -= 1;
        if( l == 0 ){
            cout << dp[r] << " " << zero[r] << endl;
        }
        else{
            cout << (dp[r] ^ dp[l-1]) << " " << zero[r] - zero[l-1] << endl;
        }
    }
}