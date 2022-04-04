#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include <vector>
using namespace std;
#define INF 1e10
struct Point{
	double x,y;
	Point( double x = 0, double y = 0) : x(x), y(y){
	}
};

bool xCompare(const Point &p1, const Point &p2){
	return p1.x < p2.x;
}

bool yCompare(const Point &p1, const Point &p2){
	return p1.y < p2.y;

}

double dis(Point &p1, Point &p2){
	return (p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y);

}

double bruteForce(vector<Point> &point_set, int left, int right){
	double min_dist = INF;
	for(int i = left; i < right; i++){
		for( int j = i + 1; j < right; j++){
			min_dist = min(min_dist, dis(point_set[i], point_set[j]));
		}
	}
	return min_dist;
}

double stripCloset(vector<Point> &point_set, int left, int right, int mid, double dist_min){
	Point point_mid = point_set[mid];
	vector<Point> splitted_points;
    for( int i = left; i < right; i++)
        if (abs(point_set[i].x - point_mid.x) <= dist_min)
        	splitted_points.push_back(point_set[i]);
    sort(splitted_points.begin(), splitted_points.end(), yCompare);
    double smallest = INF;
    int l = splitted_points.size();
    for(int i = 0; i < l; i++){
    	for(int j = i + 1; j < l && dis(splitted_points[i], splitted_points[j]) < dist_min; j++){
    		double d = dis(splitted_points[i], splitted_points[j]);
    		smallest = min(smallest, d);

		}
	}
	return smallest;
}
double minimalDis(vector<Point> &point_set, int left, int right){
	if ((right - left) <= 3)
		return bruteForce(point_set, left, right);
	int mid = (left+right)/ 2;
	double dist_left = minimalDis(point_set, left, mid);
	double dist_right = minimalDis(point_set, mid+1, right);
	double dist_min = min(dist_left, dist_right);
	return min(dist_min, stripCloset(point_set, left, right, mid, dist_min));
}
int main(){
	int n;
	double x, y;
	cin >> n;
	vector< Point > point_set;
	long long int sum = 0;

	for(int i= 0 ; i < n; i++){
		cin >> x;
		sum += x;
		point_set.push_back(Point(i, sum));
	}

	sort(point_set.begin(), point_set.end(), xCompare);
	int ans = minimalDis(point_set, 0, n);
	cout << ans << endl;
}
