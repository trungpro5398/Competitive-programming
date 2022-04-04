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
    int q;
    cin >> q;
    while(q--){
        string s;
        int x, y;
        vector<ii> v;
        cin >> s;
        if(s == "D"){
            ii temp = v.back();
            cout << temp.fi << " " << temp.se << endl;
            v.pop_back();
        }
        else{
            cin >> x >> y;
            v.pb(mp(x, y));
        }
    }
}