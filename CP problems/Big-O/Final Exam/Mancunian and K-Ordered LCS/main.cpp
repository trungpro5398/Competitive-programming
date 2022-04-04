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
int dp[2005][2005][6];
int A[2005];
int B[2005];
int lcs(int a[],int i,int b[],int j,int k){
	if(i==-1 or j==-1)
		return 0;
	if(dp[i][j][k] != -1){
		return dp[i][j][k];
	}
	if(a[i] == b[j]){
		return 1+lcs(a,i-1,b,j-1,k);
	}
	int op1=lcs(a,i-1,b,j,k);
	int op2=lcs(a,i,b,j-1,k);
	int op3 = -1;
    if(k>0){
        op3=1+lcs(a,i-1,b,j-1,k-1);
    }
	return dp[i][j][k]=max(op1,max(op2,op3));
}
int main(){
	int i,j,n,m,k;
	cin >> n >> m >> k;
	rep(i,0,n)
		cin >> A[i];
    rep(i,0,m)
        cin >> B[i];
	memset(dp,-1,sizeof dp);
	cout<<lcs(A,n-1,B,m-1,k);
    return 0;
}
