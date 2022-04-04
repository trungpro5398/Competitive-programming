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

int main(){

    int t;
    cin >> t;
    up(t1,1,t){

        string s, s1, s2, s3;
        cin >> s;
        s1 = s;
        s2 = s;
        s3 = s;
        int n = s.length();
        rep(i,0,n){
           
            rep(j,i+1,n){
                s1 = s;
                swap(s1[i],s1[j]);
                if(s1[0] == '0')
                    continue;
                if( s2 < s1 )
                    s2 = s1;
                if( s3 > s1)
                    s3 = s1;
            }
        }
        cout << "Case #" << t1 << ": " << s3 << " " << s2 << endl; 
    }
}