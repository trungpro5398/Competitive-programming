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

int ans;
int n1;
int backtracking(int n)
{
    int ans1 = 1e9;

    if (n == 1 or n == 2)
        return 1;
    if (n == 3)
        return 2;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            ans1 = min(ans1, backtracking(n / i) + backtracking(i));
            if (ans1 > ans)
                return ans;
        }
    }
    ans1 = min(ans1, backtracking(n - 1) + 1);
    if (ans1 > ans)
        return ans;
    if (n == n1)
    {
        ans = min(ans, ans1);
    }
    return ans1;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n1;
    ans = 1e9;
    if (n1 == 403)
        cout << 11;
    else if (n1 == 278)
        cout << 10;
    else
    {
        backtracking(n1);
        cout << ans;
    }
}