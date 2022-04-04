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

int main()
{
     int t,i,j,n,a[100000],m,temp;


    cin >> n;


    rep(i,0,n)
    cin >> a[i]

    cin >> m;
    rep(i,0,m){
        cin  >> temp;
        rep(j,0,n)
            if(a[j] > temp)
                a[j]--;
    }
    rep(i,0,n)
    cout<< a[i] << " ";


}
