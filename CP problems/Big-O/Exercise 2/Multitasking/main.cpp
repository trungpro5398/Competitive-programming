#include <bits/stdc++.h>

#define bug(x) cout << #x << " = " << x << endl;
#define fr(a) freopen(a, "r", stdin);
#define fw(a) freopen(a, "w", stdout);
#define tc()   \
    int tc;    \
    cin >> tc; \
    for (int _tc = 1; _tc <= tc; _tc++)
#define up(i, l, r) for (int i = l; i <= r; i++)
#define down(i, r, l) for (int i = r; i >= l; i--)
#define rep(i, l, r) for (int i = l; i < r; i++)
#define pb push_back
#define mp make_pair
#define ins insert
#define fi first
#define se second
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;

bool check(bitset<1000001> &bs, int st, int end)
{
    rep(i, st, end and i <1000001 ){
        if(bs[i]){
            return true;
        }
        bs[i] = true;
    }
    return false;
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n, m;
    while (cin >> n >> m)
    {
        if (n == 0 and m == 0)
            break;
        bitset<1000001> bs;
        bool ok = false;
        rep(i, 0, n)
        {
            ll x, y;
            cin >> x >> y;
            if( !ok )
                ok = check(bs, x, y);
        }
        rep(i, 0, m)
        {
            ll x, y, l;
            cin >> x >> y >> l;
            while( !ok and x < 1000001){
                ok = check(bs, x, y);
                x += l;
                y += l;
            }
        }
       
        if (!ok)
            cout << "NO CONFLICT" << endl;
        else
            cout << "CONFLICT" << endl;
    }
}