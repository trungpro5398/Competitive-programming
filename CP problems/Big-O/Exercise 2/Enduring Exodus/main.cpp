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
vector<int> v;

int calc(int a, int b, int c)
{
    return max(abs(v[a] - v[c]), abs(v[b] - v[c]));
}
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n, k;
    cin >> n >> k;
    k++;
    string s;
    cin >> s;
    rep(i, 0, n)
    {
        if (s[i] == '1')
            continue;
        v.pb(i + 1);
    }
    int ans = 1e9;
    for (int i = 0, j = 0; i + k <= v.size(); i++)
    {
        while (j + 1 < i + k && calc(i, i + k - 1, j) >= calc(i, i + k - 1, j + 1))
            j++;
        ans = min(ans, calc(i, i + k - 1, j));
    }
    cout << ans << endl;
}