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
vector<int> G[100005];
bool visited[100005];
int in[100005], out[100005], ts,v[100005],v1[100005];
int cnt;
vector<int> s;
vector<int> s1;
vector <int>::iterator it;
void dfs(int x)
{
	cnt++;
	visited[x] = true;
	s.push_back(x);
	for (int i = 0; i <G[x].size(); ++i)
	{
		if (!visited[G[x][i]])
			dfs(G[x][i]);
	}
	s1.insert(s1.begin(),x);
}
bool check(int x, int y)
{
	if (v[x] <= v[y] && v1[x]<=v1[y])
		return true;
	return false;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t,i,j;
    int n;
    cin>>n;
    rep(i,0,n-1)
    {
    	int a,b;
    	cin>>a>>b;
    	G[a].pb(b);
    	G[b].pb(a);
    }
    dfs(1);
    int q;
    cin>>q;
    rep(i,0,n){
        v[s[i]] = i;
        v1[s1[i]] = i;
    }
    while (q--)
    {
    	int a,x,y;
    	cin>>a>>x>>y;
    	if ((!a && check(x,y)) || (a && check(y,x)))
    		cout<<"YES\n";
    	else
    		cout<<"NO\n";
    }
    return 0;
}
