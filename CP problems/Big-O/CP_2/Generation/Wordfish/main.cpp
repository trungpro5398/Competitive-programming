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
typedef pair<string, int> si;

int main()
{
    string s;
    while (cin >> s)
    {
        vector<string> perm;
        perm.pb(s);
        string clone = s;
        for (int cnt = 0; prev_permutation(s.begin(), s.end()) && cnt < 10; cnt++)
            perm.push_back(s);
        s = clone;
        for (int cnt = 0; next_permutation(s.begin(), s.end()) && cnt < 10; cnt++)
            perm.push_back(s);
        vector<si> a;
        for (string u : perm)
        {
            int ans = INT_MAX;
            for (int j = 0; j < u.size() - 1; j++)
            {
                int minV = abs(u[j] - u[j + 1]);
                ans = min(ans, minV);
            }
            a.push_back({u, ans});
        }
        sort(a.begin(), a.end(), [](const si &A, const si &B)
             { return (A.se == B.se) ? A.fi < B.fi : A.se > B.se; });
        cout << a[0].fi << a[0].se << '\n';
    }
}