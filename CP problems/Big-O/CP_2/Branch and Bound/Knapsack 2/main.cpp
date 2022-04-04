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
#define _io                           \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;
int N, W;

ll ans = 0;

void backtracking(vector<int> &w, vector<int> &v, int sum, ll total, int index)
{
    rep(i, index, N)
    {
        if (sum + w[i] <= W)
        {
            ans = max(ans, total + v[i]);
            backtracking(w, v, sum + w[i], total + v[i], i + 1);
        }
    }
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> N >> W;
    vector<int> v(N, 0);
    vector<int> w(N, 0);
    rep(i, 0, N)
    {
        cin >> w[i] >> v[i];
    }
    rep(i, 0, N)
    {
        backtracking(w, v, 0, 0, i);
    }
    cout << ans << endl;
}