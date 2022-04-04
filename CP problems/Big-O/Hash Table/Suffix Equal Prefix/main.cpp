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

ll getHashS(int i, int j) {
    if (i <= 0)
        return hashS[j];

    return hashS[j] - hashS[i - 1] * POW[j - i + 1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    // Precompute POW
    POW[0] = 1;
    rep(i,1,MAXN) // O(MAXN)
    {
      POW[i] = (POW[i - 1] * base) ;

    }

    string s;
    up(tc,1,t){
        cin >> s;

        int n = s.length();

        // Precompute hashS
        hashS[0] = s[0] - 'a';
        rep(i,1,n) // O(|S|)
            hashS[i] = hashS[i - 1] * base + s[i] - 'a';

        int cnt = 0;
        rep(i,0,n-1) { // O(|S|)
            if (hashS[i] == getHashS(n - 1 - i, n - 1))
                cnt++;
        }

        cout << "Case " << tc << ": " << cnt << endl;
    }

    return 0;
}
