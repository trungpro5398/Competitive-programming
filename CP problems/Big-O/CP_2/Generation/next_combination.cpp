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

bool next_combination(int n, int k, vector<int> &a)
{
    int i = k - 1;
    while (i >= 0 && a[i] == n - k + i + 1)
    {
        i--;
    }
    if (i < 0)
    {
        return false;
    }
    a[i]++;
    for (int j = i + 1; j < k; j++)
    {
        a[j] = a[j - 1] + 1;
    }
    return true;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    up(i, 1, k)
    {
        cin >> a[i];
    }
    do
    {
        rep(i, 0, k)
        {
            cout << a[i] << " ";
        }
        cout << endl;

    }
    while(next_combination(n, k, a);
    return 0;
}