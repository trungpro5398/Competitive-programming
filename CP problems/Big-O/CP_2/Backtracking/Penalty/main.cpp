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

int res;
string cur;

int f(string s)
{
    int rem1 = 5, rem2 = 5, score1 = 0, score2 = 0;
    rep(i, 0, s.size())
    {
        if (i % 2 == 0)
        {
            score1 += s[i] - '0';
            rem1--;
        }
        else
        {
            score2 += s[i] - '0';
            rem2--;
        }

        if (score1 + rem1 < score2)
            return i + 1;
        if (score2 + rem2 < score1)
            return i + 1;
    }
    return 10;
}

void brute(int pos, string &s)
{
    if (cur.size() == s.size())
    {
        res = min(res, f(cur));
        return;
    }

    if (s[pos] == '?')
    {
        cur.pb('0');
        brute(pos + 1, s);
        cur.pop_back();
        cur.pb('1');
        brute(pos + 1, s);
        cur.pop_back();
    }
    else
    {
        cur.pb(s[pos]);
        brute(pos + 1, s);
        cur.pop_back();
    }
}
int main()
{
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    string s;
    int n;
    cin >> n;
    while (n--)
    {
        cin >> s;
        res = 1e9;
        brute(0, s);
        cout << res << endl;
    }
}