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

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    ll n, temp;
    cin >> n;
    ll l = 1, r = 3 * n, mid = 3 * n;
    while( l < r ){
        mid = (l+r)/2;
        ll cnt = mid / 3 + mid / 5 + mid / 7 - mid / 15 - mid / 21 - mid / 35 + mid / 105;
        
        if( cnt >= n ){
            r = mid;
        }
        else{
            l = mid + 1;
        }
    }
    cout << r;
}