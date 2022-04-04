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
#define v2d(i) vector<vector<i>>;
#define v1d(i) vector<i>;
#define map_1(i,j) map<i,j>;
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll,ll> ii;

int main(){

    int n, m;
    cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(m));
    vector<int> v;
    up(i,0,n-1) up(j,0,m-1) {
        cin >> a[i][j];
        v.pb(a[i][j]);
    }
    int x, y;
    cin >> x >> y;
    x -= 1;
    y -= 1;
    int ans = a[x][y];
    sort(v.begin(), v.end());
    int cnt = 0;
    for(int i; i < v.size(); i++) {
        
        if(v[i] > ans) {
            cnt += 1;
            ans = v[i];
        }
    }
    cout << cnt << endl;

}