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

int prefix(string &p, string &s)
{
    int best = 0;
    for (int i = 0; i < s.length() and i < p.length(); i++)
    {
        if (p.substr(p.length() - i - 1) == s.substr(0, i + 1))
        {
            best = i + 1;
        }
    }
    return best;
}
int main()
{

    int t;
    cin >> t;
    up(tc, 1, t)
    {
        int n;
        cin >> n;
        vector<string> words;
        rep(i, 0, n)
        {
            string s;
            cin >> s;
            words.pb(s);
        }
        int ans = 1e9;
        sort(words.begin(), words.end());
        do
        {
            string cur = words[0];
            rep(i, 1, words.size())
            {
                int len = prefix(cur, words[i]);
                cur += words[i].substr(len);
            }
            ans = min(ans, (int)cur.length());
        } while (next_permutation(words.begin(), words.end()));
        printf("Case %d: %d\n", tc, ans);
    }
}