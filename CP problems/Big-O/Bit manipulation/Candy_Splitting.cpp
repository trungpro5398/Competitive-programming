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

int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    up(tc, 1, t)
    {
        cout << "Case #" << tc << ": ";
        int n;
        cin >> n;
        vector<int> a(n);
        for(int& i : a)
            cin >> i;
        int ans = 0;
        for(int i : a)
            ans ^= i;
        if (ans != 0)
            cout << "NO" << endl;
        else
        {
            int maxV = accumulate(a.begin(), a.end(), 0);
            int minV = *min_element(a.begin(), a.end());
            int maxC = maxV - minV;
            cout << maxC << endl;
        }
    }
}