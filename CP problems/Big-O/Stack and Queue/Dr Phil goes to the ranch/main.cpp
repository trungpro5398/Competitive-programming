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
    while (t--)
    {
        int n;
        cin >> n;
        ll vis[n] = {0};
        int a[n];
        rep(i, 0, n)
        {
            cin >> a[i];
            a[i]--;
        }
        int p = -1;
        stack<int> s;
        rep(i, 0, n)
        {
            if(vis[a[i]])
            {
                if (s.top() == a[i])
                {
                     do
                     {
                         cout<<s.top()+1<<" ";
                         s.pop();
                         
                     }while(!s.empty() && vis[s.top()]==2);
                }
                else
                    vis[a[i]]++;
            }
            if (vis[a[i]] == 0)
            {
                rep(j, p+1, a[i])
                {
                    s.push(j);
                    vis[j] = 1;
                }
                vis[a[i]] = 1;
                p = a[i];
                cout << p + 1 << " ";
            }
            
        }
        while (!s.empty())
        {
            cout << s.top() + 1 << " ";
            s.pop();
        }
        cout << endl;
    }
}