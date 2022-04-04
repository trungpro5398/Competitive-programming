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
int vis[1000015];
int solve(vector<int> &a, int n)
{
    int lo = n/2;
    int hi = n;
    while (lo < hi) {
        int mi = lo + (hi -lo)/2;
        // cout << mi << " " <<  lo << " " << hi << endl;
        bool valid = true;
        if (mi < n - mi) {
            valid = false;
        }
        for (int i = 0; i < n -mi; i++) {
            if (a[i] < 2* a[i + mi])
                valid = false;
        }
        if (valid)
            hi = mi;
        else
            lo = mi+1;
    }
    return hi;
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    vector<int> a(n);
    rep(i, 0, n)
    {
        cin >> a[i];
    }
    sort(a.begin(), a.end(), greater<int>());
    cout << solve(a, n) << endl;
}