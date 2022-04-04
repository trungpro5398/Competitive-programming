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
int n, m;
vector<int> DSK[20005];

void dfs(vector<int> &vis, int &cnt){
    vis[cnt] = 1;
    for (int i=0;i<DSK[cnt].size();i++){
        if (!vis[DSK[cnt][i]]){
            dfs(vis, DSK[cnt][i]);
        }
    }
}
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    cin >> n;
    up(i,1,n){
        int x;
        cin >> x;
        DSK[x].pb(i);
        DSK[i].pb(x);

    }

    vector<int> vis(n+1, 0);
    int cnt = 0;
    up(i,1,n){
        if (!vis[i]){
            cnt++;
            dfs(vis, i);
        }
    }
    cout << cnt << endl;
}