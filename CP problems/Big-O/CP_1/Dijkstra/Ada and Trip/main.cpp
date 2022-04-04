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
struct cmpp
{
	bool operator()(pair<int,int> a,pair<int,int> b)
	{
		return a.second>b.second;
	}
};
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n, m, q;
    cin >> n >> m >> q;
    vector<vector<ii>> adj(n);
    up(i,0,m-1){
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].pb(mp(v,w));
        adj[v].pb(mp(u,w));
    }
    while(q--){
        int s1;
        cin >> s1;
        vector<bool> vis(n, false);
        priority_queue<ii, vector<ii>, cmpp> pq;
        pq.push(mp(s1, 0));
        int max_dist = -1;
        int cnt = -1;
        while(!pq.empty()){
            ii cur = pq.top();
            pq.pop();
            if(vis[cur.fi]) continue;
            vis[cur.fi] = true;
            
            rep(i,0,adj[cur.fi].size()){
                ii next = adj[cur.fi][i];
                if(!vis[next.fi]) pq.push(mp(next.fi, cur.se+next.se));
            }
            if(cur.se == max_dist){
                cnt++;
            }
            else if(cur.se > max_dist){
                max_dist = cur.se;
                cnt = 1;
            }
        }
        cout << max_dist << " " << cnt << endl;

    }
}