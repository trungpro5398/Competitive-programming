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
    int n, m, k;
    cin >> m >> n >> k;
    vector<std::vector<int>> a(m+2, std::vector<int>(n+2, 0));
    rep(i, 0, m)
    {
        rep(j, 0, n)
        {
            cin >> a[i + 1][j + 1];
        }
    }
    
    int b[k];
    rep(i, 0, k)
    {
        cin >> b[i];
    }

    vector<int> v;
    up(i, 1, m)
    {
        up(j, 1, n)
        {
            v.pb(a[i - 1][j - 1] + a[i - 1][j + 1] + a[i + 1][j - 1] + a[i + 1][j + 1] + a[i - 1][j] + a[i][j - 1] + a[i][j + 1] + a[i + 1][j]);
        }
    }
    sort(v.begin(), v.end());
    rep(i,0,k){
        auto temp = lower_bound(v.begin(), v.end(), b[i]) - v.begin();
        auto temp2 = upper_bound(v.begin(), v.end(), b[i]) - v.begin();
        if(temp != temp2)
            cout << 1 << " ";
        else
            cout << 0 << " ";
    }
    cout << endl;
}