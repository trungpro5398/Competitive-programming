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
int n, m;
bool sovle(vector<vector<char>> &board, int i, int j, int p, vector<vector<bool>> &visit)
{
    if (i < 0 || i >= m || j < 0 || j >= n || p < 0 || board[i][j] == '#')
        return false;
    if (board[i][j] == 'x' and p == 0)
    {
        return true;
    }
    if (!visit[i][j])
    {
        visit[i][j] = true;
        int k = board[i][j] == 's' ? p - 1 : p;
        if (sovle(board, i + 1, j, k, visit) || sovle(board, i - 1, j, k, visit) || sovle(board, i, j + 1, k, visit) || sovle(board, i, j - 1, k, visit))
            return true;
        visit[i][j] = false;
    }
    return false;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int z;
    int a, b;
    cin >> m >> n >> z;
    vector<vector<char>> board(m, vector<char>(n, 32));
    vector<vector<bool>> visit(m, vector<bool>(n, 0));
    rep(i, 0, m)
    {
        rep(j, 0, n)
        {

            cin >> board[i][j];
            if (board[i][j] == '@')
            {
                a = i;
                b = j;
            }
        }
    }
    if (sovle(board, a, b, z, visit))
    {
        cout << "SUCCESS" << endl;
    }
    else
    {
        cout << "IMPOSSIBLE" << endl;
    }
    return 0;
    return 0;
}