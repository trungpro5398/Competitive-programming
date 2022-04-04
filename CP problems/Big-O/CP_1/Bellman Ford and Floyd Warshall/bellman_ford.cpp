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

const int INF = 1e9;
struct Edge {
    int u, v, w;
    Edge(int u, int v, int w) : u(u), v(v), w(w) {}
};
vector<int> dist, path;
int bellmanFord(vector<Edge> edges, int n, int m, int s){
    dist.resize(n+1, INF);
    path.resize(n+1, -1);
    dist[s] = 0;
    int u, v, w;
    rep(i,1,n){
        rep(j,0,m){
            u = edges[j].u;
            v = edges[j].v;
            w = edges[j].w;
            if (dist[u] < INF && dist[u] + w < dist[v]){
                dist[v] = dist[u] + w;
                path[v] = u;
            }
        }
    }
    // check negative cycle
    rep(j,0,m){
        u, v, w = edges[j].u, edges[j].v, edges[j].w;
        if (dist[u] < INF && dist[u] + w < dist[v]){
            return false;
        }
    }
    return true;
}
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);

}