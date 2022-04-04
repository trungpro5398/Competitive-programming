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
#define MAXN 400005

ll Pow10[MAXN];
ll res = 0;
bool isRes = false;

int get(ll val, int pos)
{
    if (pos == 19)
        return val / Pow10[pos - 1];
    return (val % Pow10[pos]) / Pow10[pos - 1];
}

void Find(int pos, ll val, ll cur_var, bool isLower, vector<int> num)
{
    if (isRes)
        return;
    if (pos == 0)
    {
        res = cur_var;
        isRes = true;
        return;
    }

    int x = get(val, pos);
    if (isLower)
        x = 9;

    for (int i = x; i >= 0; i--)
    {
        if (num[i] == 2)
            continue;
        if (i > 0 || cur_var > 0)
            num[i]++;
        bool cur_isLower = isLower;
        if (i < x and !cur_isLower)
            cur_isLower = true;
        Find(pos - 1, val, cur_var + i * Pow10[pos - 1], cur_isLower, num);
        if (i > 0 || cur_var > 0)
            num[i]--;
    }
}
int main()
{
    _io;
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    Pow10[0] = 1;
    up(i, 1, 18)
    {
        Pow10[i] = Pow10[i - 1] * 10;
    }
    ll n;
    while (cin >> n)
    {
        vector<int> num(10, 0);
        isRes = false;
        Find(19, n, 0, false, num);
        cout << res << endl;
    }
}