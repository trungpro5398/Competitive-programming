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
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n, m;
    cin >> n;
    int a[n+1];
    a[n] = 0;
    up(i,0,n-1)
    {
        cin >> a[i];
    }
    cin >> m;
    int b[m+1];
    b[m] = 0;
    up(i,0,m-1)
    {
        cin >> b[i];
    }
    int l = 0, l1 = 0, temp = a[0], temp1 = b[0], cnt = 0;
    vector<int> v, v1;
    while(l < n && l1 < m)
    {
        if(temp == temp1){
            temp = a[l+1];
            temp1 = b[l1+1];
            l++;
            l1++;
            cnt++;
        }
        else if( temp > temp1){
            temp1 += b[l1+1];
            l1++;
        }
        else if( temp < temp1){
            temp += a[l+1];
            l++;
        }
    }
    if( temp != temp1 )

        cnt = -1;
    cout << cnt ;
}