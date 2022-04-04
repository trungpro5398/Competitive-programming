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

string s;
map<char, bool> letters;
set<pair<char, char>> edges;
vector<string> lines;
vector<vector<char>> adj;
vector<char> order;

void dfs(char c){
    letters[c] = true;
    for (auto i : adj[c]){
        if (!letters[i]){
            dfs(i);
        }
    }
    order.pb(c);
}
int main()
{
    adj.resize(300);
    while (getline(cin, s), s.compare("#") != 0)
    {
        lines.pb(s);
    }
    for (string line : lines)
    {
        assert(line.size() <= 20);
        for (char c : line)
        {
            letters[c] = false;
        }
    }

    rep(i, 1, lines.size())
    {
        string &pre = lines[i - 1];
        string &cur = lines[i];
        rep(j, 0, j < pre.size() and j < cur.size())
        {
            if (pre[j] != cur[j])
            {

                if (!edges.count(mp(pre[j], cur[j])))
                {
                    edges.insert(mp(pre[j], cur[j]));
                    adj[pre[j]].pb(cur[j]);
                }
                break;
            }
        }
    }

    for(auto p: letters){
        char c = p.fi;
        bool vs = p.se;
        if(!vs){
            dfs(c);
        }
    }

    down(i,order.size()-1, 0){
        cout << order[i];
    }
}