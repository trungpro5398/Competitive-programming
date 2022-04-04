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

struct Train{
    int a, b, id;
};
int convert(string s){
    return ((s[0] - '0') * 10 + s[1] - '0') * 60 + (s[3] - '0') * 10 + s[4] - '0';
}
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    up(i,1,t){
        int T;
        int na, nb;
        string a, b;
        cin >> T >> na >> nb;
        vector<Train> trains;
        rep(i,0, na){
            cin >> a >> b;
            trains.pb(Train{convert(a), convert(b), 0});
        }
        rep(i,0, nb){
            cin >> a >> b;
            trains.pb(Train{convert(a), convert(b), 1});
        }
        sort(trains.begin(), trains.end(), [](const Train &a, const Train &b){
            return a.a < b.a;
        });
        priority_queue<int, vector<int>, greater<int>> pq[2];
        int start[2] = {0};
        rep(i,0, trains.size()){
            int d = trains[i].id;
            if(!pq[d].empty() and pq[d].top() <= trains[i].a){
                pq[d].pop();
            }
            else{
                start[d] ++;
            }
            pq[1-d].push(trains[i].b + T) ;
        }
        cout << "Case #" << i << ": " << start[0] << " " << start[1] << endl;

    }
}