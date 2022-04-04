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

ll solve(vector<int> &v, int left, int right, int height)
{
    if (left > right)
        return 0;
    int mid = left;
    for (int i = left; i <= right; ++i)
    {
        if (v[i] < v[mid])
            mid = i;
    }
    int all = right - left + 1;

    int recersive = v[mid] - height + solve(v, left, mid - 1, v[mid]) + solve(v, mid + 1, right, v[mid]);
    return min(all, recersive);
}
int main()
{
    int n;
    cin >> n;

    vector<int> v(n);

    rep(i, 0, n) cin >> v[i];
    cout << solve(v, 0, n - 1, 0) << endl;
}