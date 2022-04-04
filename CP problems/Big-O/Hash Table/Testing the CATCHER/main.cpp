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

int lis(const vector<int>& a){

    int length = 0;
    vector<int> dp(a.size(), 1);
    rep(i,1,a.size()){
        rep(j,0,i){

            if(a[i] > a[j] && dp[i] < dp[j] + 1){

                dp[i] = dp[j] + 1;
                length = max(length, dp[i]);
            }
        }
    }
    return length;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, i, j,max1, len[100000];
    vector<int> a(100000,0);
    int kase = 0;
    bool End = false;
    while (cin >> a[0]) {
        if (a[0]==-1) break;
        if (End) cout << endl;
        End = true;
        n = 0;
        while (cin >> a[++n])
            if (a[n]==-1) break;
        max1 = lis(a);
        printf("Test #%d:\n  maximum possible interceptions: %d\n",++kase,max1);
    }

    return 0;
}
