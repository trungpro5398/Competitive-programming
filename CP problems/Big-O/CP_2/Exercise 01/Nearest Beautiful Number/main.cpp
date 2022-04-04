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

int n, k;
string s;

int calc(string str)
{
    set<char> s;

    for (char ch : str)
        s.insert(ch);
    return s.size();
}

int calc1(string str)
{
    int cnt = 0;
    for (char ch : str)
        cnt = cnt * 10 + ch - 48;
    return cnt;
}
string solve()
{
    cin >> s >> k;
    n = s.size();
    if (calc(s) <= k)
        return s;
    down(i, n - 1, 0)
    {
        string t = s;
        for (char j = s[i] + 1; j <= '9'; j++)
        {
            set<char> S;
            rep(k, 0, i)
                S.insert(s[k]);
            t[i] = j;
            S.insert(j);
            if (calc(t.substr(0, i + 1)) > k)
                continue;
            char p = calc(t.substr(0, i + 1)) < k ? '0' : *S.begin();
            rep(k, i + 1, n)
                t[k] = p;
            if (calc1(t) >= calc1(s))
                return t;
        }
    }
}
int main()
{
    int t;
    cin >> t;
    while (t--)
        cout << solve() << endl;
}