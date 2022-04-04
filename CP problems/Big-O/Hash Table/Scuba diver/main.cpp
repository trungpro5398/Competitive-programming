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
#define inf 0x3f3f3f3f
int main()
{
    int k;
    cin >> k;
    while(k--){
        int t, a, n;
        cin >> t >> a >> n;
        int dp[n+1][t+1][a+1];
        vector<int> oxy(n+1), nit(n+1), weight(n+1);
        rep(i,0,n)
            cin>> oxy[i] >> nit[i] >> weight[i] ;
        up(i,0,t){
            up(j,0,a){
                if(i <= oxy[0] && j <= nit[0]){
                    dp[0][i][j] = weight[0];
                }
                else{
                    dp[0][i][j] = inf;
                }
            }
        }
        dp[0][0][0]=0;
        rep(i,1,n){
            up(j,0,t){
                up(k,0,a){

                    dp[i][j][k] = min(dp[i-1][j][k], weight[i] + dp[i-1][max(0, j-oxy[i])][max(0, k-nit[i])]);
                }
            }

        }
        cout << dp[n-1][t][a] << endl;
    }

    return 0;
}
