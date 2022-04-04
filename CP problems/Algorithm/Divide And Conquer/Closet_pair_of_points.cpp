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
    Point(double x = 0, double y = 0) : x(x), y(y) {}
};

bool xCompare(const Point &p1, const Point &p2)
{
    return p1.x < p2.x;
}

bool yCompare(const Point &p1, const Point &p2)
{
    return p1.y < p2.y;
}

double distance(const Point &p1, const Point &p2)
{
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}
double bruteForce(vector<Point> &point_set, int left, int right)
{
    double min_distance = INF;
    for (int i = left; i < right; i++)
    {
        for (int j = i + 1; j <= right; j++)
        {
            min_distance = min(min_distance, distance(point_set[i], point_set[j]));
        }
    }
    return min_distance;
}

double stripClosest(vector<Point> &point_set, int left, int right, int mid, double dist_min)
{
    Point point_mid = point_set[mid];
    vector<Point> splitted_points;
    rep(i, left, right) if (abs(point_set[i].x - point_mid.x) <= dist_min)
        splitted_points.pb(point_set[i]);

    sort(splitted_points.begin(), splitted_points.end(), [](Point a, Point b)
         { return a.y < b.y; });

    // sort(splitted_points.begin(), splitted_points.end(), yCompare);

    double smallest = INF;

    int l = splitted_points.size();

    rep(i, 0, l)
    {
        rep(j, i + 1, l && (splitted_points[j].y - splitted_points[i].y) <= dist_min)
        {
            smallest = min(smallest, distance(splitted_points[i], splitted_points[j]));
        }
    }

    return smallest;
}
double minimalDIstance(vector<Point> &point_set, int left, int right)
{
    if (right - left <= 3)
        return bruteForce(point_set, left, right);

    int mid = (left + right) / 2;
    double dist_left = minimalDIstance(point_set, left, mid);
    double dist_right = minimalDIstance(point_set, mid + 1, right);
    double dist_min = min(dist_left, dist_right);
    return min(dist_min, stripClosest(point_set, left, right, mid, dist_min));
}
int main(int argc, char)
{
    int n;
    double x, y;
    cin >> n;
    vector<Point> point_set;

    rep(i, 0, n)
    {
        cin >> x >> y;
        point_set.pb(Point(x, y));
    }

    sort(point_set.begin(), point_set.end(), [](Point a, Point b)
         { return a.x < b.x; });
    // sort(point_set.begin(), point_set.end(), xCompare);

    double ans = minimalDIstance(point_set, 0, n);
    cout << fixed << setprecision(2) << ans << endl;
}