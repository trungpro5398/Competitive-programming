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
const ll MAXN = 1000007;
ll POW[MAXN]; // POW[i] is equal to base^i
ll hashS[MAXN]; // hashS[i] is hash value from s[0..i]
ll mod = 1e9 + 7;
ll computeHash(string s){
    ll res = 0;
    rep(i,0,s.length()){
        res += (s[i] * POW[i]) % mod;
    }
    return res;
}
set<ll> ans;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);




    int n,m;
    cin >> n >> m;
    vector<string> ans;
    rep(i,0,n){
        string s;
        cin >> s;

        ans.push_back(s);

    }
    sort(ans.begin(), ans.end());

    rep(i,0,m){

        string s;
        cin >> s;
        string res = s;
        bool as = false;
        rep(j,0,s.length()){

            up(k1,'a','c'){
                char k = (char) k1;
                if( k != s[j]){

                    res[j] = k;
                    if(binary_search(ans.begin(), ans.end(),res)){
                        as = true;
                        break;
                    }
                    res[j] = s[j];
                }
                if(as)
                    break;
            }

            if(as)
                break;
        }
        as ? cout << "YES" << endl : cout << "NO" << endl;
    }

    return 0;
}
