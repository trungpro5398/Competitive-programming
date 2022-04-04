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