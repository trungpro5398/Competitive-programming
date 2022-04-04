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

bool next_permutation(string &s)
{
    int i = s.size() - 2;
    while (i >= 0 and s[i] >= s[i + 1])
        i--;
    if (i < 0)

        return false;
    int k = s.size() - 1;
    while (s[i] >= s[k])
        k--;
    swap(s[i], s[k]);
    i++;
    k = s.size() - 1;
    while (i < k)
    {
        swap(s[i], s[k]);
        i++;
        k--;
    }
    return true;
}
// bool nextpermutation(string &s)
// {
//     int len = s.size();
//     int i = len - 2;
//     while (i >= 0 && s[i] >= s[i + 1])
//     {
//         i--;
//     }
//     if (i < 0)
//     {
//         return false;
//     }
//     else
//     {
//         int index = i + 1;
//         while (index < len && s[index + 1] > s[i])
//             index++;
//         swap(s[i], s[index]);
//         reverse(s.begin() + i + 1, s.end());
//         return true;
//     }
// }
int main()
{

    string s;
    while (cin >> s)
    {
        if (s == "#")
            break;
        for (auto c : s)
        {
            assert('a' <= c && c <= 'z');
        }
        // bool val = next_permutation(s.begin(), s.end());
        bool val = next_permutation(s);
        if (val == false)
        {
            cout << "No Successor\n";
        }
        else
            cout << s << "\n";
    }
}