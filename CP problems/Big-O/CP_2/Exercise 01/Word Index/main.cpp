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

map<string, int> res;

void pre()
{
    int cnt = 1;
    char s[6];
    for (s[0] = 'a'; s[0] <= 'z'; s[0]++)
    {
        s[1] = '\0';
        res[string(s)] = cnt++;
    }
    for (s[0] = 'a'; s[0] <= 'z' - 1; s[0]++)
        for (s[1] = s[0] + 1; s[1] <= 'z'; s[1]++)
        {
            s[2] = '\0';
            res[string(s)] = cnt++;
        }

    for (s[0] = 'a'; s[0] <= 'z' - 2; s[0]++)
        for (s[1] = s[0] + 1; s[1] <= 'z' - 1; s[1]++)
            for (s[2] = s[1] + 1; s[2] <= 'z'; s[2]++)
            {
                s[3] = '\0';
                res[string(s)] = cnt++;
            }

    for (s[0] = 'a'; s[0] <= 'z' - 3; s[0]++)
        for (s[1] = s[0] + 1; s[1] <= 'z' - 2; s[1]++)
            for (s[2] = s[1] + 1; s[2] <= 'z' - 1; s[2]++)
                for (s[3] = s[2] + 1; s[3] <= 'z'; s[3]++)
                {
                    s[4] = '\0';
                    res[string(s)] = cnt++;
                }

    for (s[0] = 'a'; s[0] <= 'z' - 4; s[0]++)
        for (s[1] = s[0] + 1; s[1] <= 'z' - 3; s[1]++)
            for (s[2] = s[1] + 1; s[2] <= 'z' - 2; s[2]++)
                for (s[3] = s[2] + 1; s[3] <= 'z' - 1; s[3]++)
                    for (s[4] = s[3] + 1; s[4] <= 'z'; s[4]++)
                    {
                        s[5] = '\0';
                        res[string(s)] = cnt++;
                    }
}
int main()
{
    pre();
    char s[6];
    while (scanf("%s", s) != EOF)
    {

        if (res.count(string(s)) == 0)
        {
            cout << 0 << endl;
        }
        else
        {
            cout << res[string(s)] << endl;
        }
    }
}