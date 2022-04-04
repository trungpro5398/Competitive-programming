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

map<ll, ll> m;
int main()
{
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    vector<ll> v;
    rep(i, 0, n)
    {
        int a;
        cin >> a;
        v.pb(a);
        m[a] += 1;
    }
    sort(v.begin(), v.end());
    int x = 0, y = 0, z = 0;
    rep(i, 0, n - 2)
    {
        rep(j, i + 1, n - 1)
        {
            ll c = sqrt(v[i] * v[i] + v[j] * v[j]);
            if (m.find(c) != m.end() and c * c == v[i] * v[i] + v[j] * v[j])
            {
                z += m[c];
                m[c] = 0;
            }
        }
    }
    rep(i, 0, n - 2)
    {
        rep(j, i + 1, n - 1)
        {
            if (v[i] == v[j])
            {
                ll lo = lower_bound(v.begin(), v.end(), v[i] * 2) - v.begin();
                while (v[lo] >= v[i] * 2)
                    lo -= 1;
                y += lo - j;
            }
        }
    }
    for (int i = n - 1; i >= 1; i--)
    {
        int l = 0, r = i - 1;
        while (l < r)
        {
            if (v[l] + v[r] > v[i])
            {

                x += r - l;

                r--;
            }
            else

                l++;
        }
    }
    cout << x << " " << y << " " << z << endl;
}