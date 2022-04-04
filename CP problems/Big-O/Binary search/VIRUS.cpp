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

bool compare(string a, string b) {
    rep(i,0, a.size()){
        if(b[i] == '*')
            continue;
        if(a[i] != b[i])
            return false;
    }
    return true;
}
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    up(tc,1,t){
        cout << "Data set #" << tc << ":" << endl;
        int n, m;
        cin >> n;
        string bad[n];
        rep(i,0,n){
            cin >> bad[i];
        }
        cin >> m;
        up(i,1,m){
            cout << "Virus #" << i << ": ";
            string s;
            cin >> s;
            int flag = 0;
            rep(j,0,n){
                int sizea = s.size(), sizeb = bad[j].size();
                if(sizea < sizeb)
                    continue;
                rep(k,0,sizea - sizeb+1){
                    if(compare(s.substr(k, sizeb), bad[j])){
                        flag = 1;
                        break;
                    }
                }
                if(flag)
                    break;
            }
            if(flag) cout << "Nuts. This virus is illegal in Hawaii!" << endl;
            else cout << "Cool! Victor can take it with him!" << endl;
        }
        cout << endl;
    }
}