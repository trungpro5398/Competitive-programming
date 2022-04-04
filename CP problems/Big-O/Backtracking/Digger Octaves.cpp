#include <bits/stdc++.h>

using namespace std;
bool vis[20][20] ;
char mat[20][20] ;
set< vector< pair<int,int> > > res ;
int dx[] = {0 , 0 , -1 , 1};
int dy[] = {-1 , 1 , 0 , 0};
void dfs( int n, int i , int j, int cnt , vector< pair<int,int> > vect){
	
	if (mat[i][j] == '.'){
		return;
	}
	vect.push_back(make_pair(i,j));
	if( cnt  == 8 ){
		sort(vect.begin(), vect.end());
		res.insert(vect);
		vis[i][j]= 0;
		return ;
	}
	vis[i][j] = 1;
	for( int k = 0; k < 4 ; k++){
		int x = dx[k] + i;
		int y = dy[k] + j;
		if (x < 0 || y < 0 || x == n|| y == n){
			continue;
		}
		if(mat[x][y] == 'X' && vis[x][y] == 0){
			dfs(n,x,y,cnt+1, vect);
		} 
	}
	
	vis[i][j] = 0;
	
	
}
int main()
{
    ios_base::sync_with_stdio(0) ;
    int t ;
    cin >> t ;
    while(t--)
    {
        int n ;
        cin >> n ;
        res.clear() ;
        for(int i=0;i<n;i++){
        	for(int j=0;j<n;j++)
                vis[i][j] = 0 ;
		}
        
            
        
        for(int i=0; i<n; i++){
        	for(int j = 0 ; j < n; j++)
                cin >> mat[i][j] ;
		}
        
            
        
        for(int i=0; i<n; i++)
        {
		
            for(int j = 0 ; j < n; j++)
            {
                vector< pair<int,int> > vect ;
                dfs(n,i,j,1,vect) ;
            }
        }
        cout << res.size() << endl ;
    }
    return 0;
}
