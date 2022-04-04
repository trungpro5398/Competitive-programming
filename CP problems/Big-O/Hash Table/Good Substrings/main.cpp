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
const int base = 29; // base should be a prime number >= number of characters, for example 26 characters in lowercase english
const ll MAXN = 1000000;
ll POW[MAXN]; // POW[i] is equal to base^i
ll hashS[MAXN]; // hashS[i] is hash value from s[0..i]
ll mod = 1e9+7;
ll getHashS(int i, int j) {
    if (i <= 0)
        return hashS[j];

    return (hashS[j] - hashS[i - 1] * POW[j - i + 1]);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    // Precompute POW
    POW[0] = 1;
    rep(i,1,MAXN) // O(MAXN)
    {
      POW[i] = (POW[i - 1] * base) ;

    }
    ll k;
    string s1;
    string s;
    cin >> s;
    cin >> s1;
    cin >> k;
    int n = s.length();
    vector<ll> dp(n+1,0);
        // Precompute hashS
    hashS[0] = s[0];
    rep(i,1,n) // O(|S|)
    hashS[i] = hashS[i - 1] * base + s[i];


    rep(i,0,n){
        if(s1[s[i] - 'a'] == '0'){
            dp[i+1] = dp[i] + 1;
        }
        else
            dp[i+1] = dp[i];
    }

    set < ll > ans;
    rep(i,0,n){
        rep(j,i,n){
            if(dp[j+1] - dp[i] <= k){
                ll t = getHashS(i,j);
                ans.insert(t);
            }
        }
    }
    cout << ans.size();
    return 0;
}
