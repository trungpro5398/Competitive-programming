#include <bits/stdc++.h>

#define bug(x) cout << #x << " = " << x << endl;
#define fr(a) freopen(a,"r",stdin);
#define fw(a) freopen(a,"w",stdout);
#define tc() int tc;cin >> tc; for (int _tc=1;_tc<=tc;_tc++)
#define up(i,l,r) for (int i=l;i<=r;i++)
#define down(i,r,l) for (int i=r;i>=l;i--)
#define rep(i,l,r) for (int i=l;i<r;i++)
#define pb push_back
#define mp make_pair
#define ins insert
#define fi first
#define se second
using namespace std;


#define ROW 500
#define COL 500
// Direction vectors
int dRow[] = { -1, 0, 1, 0 };
int dCol[] = { 0, 1, 0, -1 };
int n,m;
// Function to check if a cell
// is be visited or not
bool isValid(bool vis[][COL],int row, int col)
{
    // If cell lies out of bounds
    if (row < 0 || col < 0
        || row >= n || col >= m)
        return false;

    // If cell is already visited
    if (vis[row][col])
        return false;

    // Otherwise
    return true;
}

// Function to perform the BFS traversal
void BFS(int grid[][COL], bool vis[][COL],
         int row, int col, int s)
{
    // Stores indices of the matrix cells
    queue<pair<int, int> > q;

    // Mark the starting cell as visited
    // and push it into the queue
    q.push({ row, col });
    vis[row][col] = true;
    int cnt = 1;
    // Iterate while the queue
    // is not empty
    while (!q.empty()) {

        pair<int, int> cell = q.front();
        int x = cell.first;
        int y = cell.second;



        q.pop();

        // Go to the adjacent cells
        for (int i = 0; i < 4; i++) {

            int adjx = x + dRow[i];
            int adjy = y + dCol[i];

            if (isValid(vis, adjx, adjy) && abs(grid[x][y] - grid[adjx][adjy]) <= s) {
                q.push({ adjx, adjy });
                vis[adjx][adjy] = true;
                cnt += 1;
            }
        }
    }
    cout << cnt << endl;
}

// Driver Code
int main()
{
    bool vis[ROW][COL];
    int arr[ROW][COL];

    int q;
    cin >> n >> m >> q;
    rep(i,0, n){
        rep(j,0, m){
            int x;
            cin >> x;
            arr[i][j] = x;
        }
    }
    // Declare the visited array
    rep(i,0,q){
        int a,b,s;
        cin >>a>>b>>s;
        memset(vis, false, sizeof vis);
        BFS(arr, vis, b-1,a-1,s );
    }



    return 0;
}
