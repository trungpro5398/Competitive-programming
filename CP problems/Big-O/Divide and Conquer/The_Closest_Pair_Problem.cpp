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
#define INF 1e9;

struct Point
{
    double x, y;

    Point(double x = 0, double y = 0) : x(x), y(y){};
};

double distance(Point a, Point b)
{
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

double bruteForce(vector<Point> point_set, int left, int right)
{
    double min_dist = INF;

    rep(i, left, right)
        rep(j, i + 1, right)
            min_dist = min(min_dist, distance(point_set[i], point_set[j]));
    return min_dist;
}

double stripClosest(vector<Point> point_set, int left, int right, int mid, double min_dist)
{
    Point point_mid = point_set[mid];
    vector<Point> splitted_points;
    rep(i, left, right)
    {
        if (abs(point_set[i].x - point_mid.x) < min_dist)
            splitted_points.pb(point_set[i]);
    }

    sort(splitted_points.begin(), splitted_points.end(), [](Point a, Point b)
         { return a.y < b.y; });

    double smallest = INF;

    int l = splitted_points.size();

    rep(i, 0, l)
        rep(j, i + 1, l && (splitted_points[j].y - splitted_points[i].y) < min_dist)
            smallest = min(smallest, distance(splitted_points[i], splitted_points[j]));

    return smallest;
}
double minimalDIstance(vector<Point> &point_set, int left, int right)
{
    if (right - left <= 3)
        return bruteForce(point_set, left, right);

    int mid = (right + left) / 2;

    double min_left = minimalDIstance(point_set, left, mid);
    double min_right = minimalDIstance(point_set, mid + 1, right);
    double min_dist = min(min_left, min_right);
    return min(min_dist, stripClosest(point_set, left, right, mid, min_dist));
}
int main()
{

    int n;

    while (cin >> n)
    {
        if (n == 0)
            break;
        vector<Point> point_set;

        rep(i, 0, n)
        {
            int x, y;
            cin >> x >> y;
            point_set.pb(Point(x, y));
        }

        sort(point_set.begin(), point_set.end(), [](Point a, Point b)
             { return a.x < b.x; });

        double ans = minimalDIstance(point_set, 0, n);
        ans >= 10000 ? cout << "INFINITY" << endl : cout << fixed << setprecision(4) << ans << endl;
    }
}