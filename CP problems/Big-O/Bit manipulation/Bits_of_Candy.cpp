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

void tokenize(string const &str, const char delim,
              vector<string> &out)
{
    // construct a stream from the string
    stringstream ss(str);

    string s;
    while (getline(ss, s, delim))
    {
        out.push_back(s);
    }
}

int invertBits(int num)
{
    // calculating the mask
    int x = 15;   // say num = 100000
    x |= x >> 1;  // 100000 | 010000 = 110000
    x |= x >> 2;  // 110000 | 001100 = 111100
    x |= x >> 4;  // 111100 | 000011 = 111111
    x |= x >> 8;  // 111111 | 000000 = 111111
    x |= x >> 16; // 111111 | 000000 = 111111

    return (num ^ x);
}
// Goobers | Caramello | Reeses_Cups & ~Reeses_Pieces & ~Reeses_Cups & Milky_Way | Hersheys

map<string, int> m{
    {"Planters", 1},
    {"Reeses_Pieces", 2},
    {"Sugar_Babies", 4},
    {"Pay_Day", 5},
    {"Hersheys", 8},
    {"Goobers", 9},
    {"Reeses_Cups", 10},
    {"Nutrageous", 11},
    {"Caramello", 12},
    {"Baby_Ruth", 13},
    {"Milky_Way", 14},
    {"Snickers", 15}};
map<int, string> m2;
int notCal(string s)
{
    if (s[0] == '~')
    {
        int cnt = 0;
        rep(i, 0, s.size())
        {
            if (s[i] == '~')
                cnt++;
            else
            {
                if (cnt % 2 == 0)
                    return m[s.substr(i, s.size() - i)];
                else
                    return invertBits(m[s.substr(i, s.size() - i)]);
            }
        }
    }
    return m[s];
}
int main()
{

    for (auto i : m)
    {
        m2[i.se] = i.fi;
    }
    int n;
    cin >> n;
    cin.ignore();
    while (n--)
    {
        string txt;
        getline(cin, txt);
        vector<string> out;
        tokenize(txt, ' ', out);
        int ans = -1;
        string k = "&";
        for (int i = 0; i < out.size(); i += 2)
        {
            if (i + 2 < out.size() and out[i + 1][0] == '&')
            {
                int temp = notCal(out[i]);
                while (i + 2 < out.size() and out[i + 1][0] == '&')
                {
                    temp &= notCal(out[i + 2]);
                    i += 2;
                }
                if (ans == -1)
                    ans = temp;
                else
                    ans |= temp;
            }
            else
            {
                if (ans == -1)
                    ans = notCal(out[i]);
                else
                    ans |= notCal(out[i]);
            }
        }
        if (m2[ans] == "")
            cout << "Unknown candy bar!" << endl;
        else
            cout << m2[ans] << endl;
    }
    return 0;
}