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

map < char, int > vis;
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n;
    string s;
    cin >> n >> s;
    for(int i=0;i<n;i++){
        vis[s[i]]++;
    }
    int cnt = 0;
    for(auto &i: vis){
        cnt += max(0,i.se-1);
    }
    cout << (cnt < 19 ? cnt : -1) << endl;
}