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
#define v2d(i) vector< vector<i> >
#define v1d(i) vector<i>
#define map_1(i,j) map<i,j>
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll,ll> ii;

v1d(int) topologicalSort (v2d(int) &graph, v1d(int) &indegree){
    int n = indegree.size();
    priority_queue<int, v1d(int), greater<int> > pq;
    rep(i, 0, n){
        if(indegree[i] == 0){
            pq.push(i);
        }
    }
    v1d(int) topoSorted;
    while(!pq.empty()){
        int cur = pq.top();
        pq.pop();
        topoSorted.pb(cur);
        for(auto& i : graph[cur]){
            indegree[i]--;
            if(indegree[i] == 0){
                pq.push(i);
            }
        }
    }
    return topoSorted;
}
int main(){
    int n, m;

    cin >> n >> m;
    v2d(int) graph(n);
    v1d(int) indegree(n);
    rep(i, 0, m){
        int u, v;
        cin >> u >> v;
        u -= 1; v -= 1;
        graph[u].pb(v);
        indegree[v]++;
    }
    v1d(int) topoSorted = topologicalSort(graph, indegree);
    if(topoSorted.size() == n){
        rep(i, 0, n){
            cout << topoSorted[i] + 1 << " ";
        }
    }
    else{
        cout << "Sandro fails.\n";
    }
    
}