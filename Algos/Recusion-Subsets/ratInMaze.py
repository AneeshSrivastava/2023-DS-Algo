n=4
ans=[]



def findPaths(maze, pos_x, pos_y, visited, ans, path):
    if pos_x==n-1 and pos_y==n-1:
        return ans.append(path)
    
    # Move Down:
    new_x= pos_x+1
    new_y=pos_y
    if isSafe(maze, visited, new_x, new_y):
        visited[new_x][new_y]=1
        path+="D"
        findPaths(maze, new_x, new_y, visited, ans, path)
        path=path[:-1]
        visited[new_x][new_y]=0

    
    # Move Left:
    new_x= pos_x
    new_y=pos_y-1
    if isSafe(maze, visited, new_x, new_y):
        visited[new_x][new_y]=1
        path+="L"
        findPaths(maze, new_x, new_y, visited,ans, path)
        path=path[:-1]
        visited[new_x][new_y]=0

    
    # Move Up:
    new_x= pos_x-1
    new_y=pos_y
    if isSafe(maze, visited, new_x, new_y):
        visited[new_x][new_y]=1
        path+="U"
        findPaths(maze, new_x, new_y, visited,ans, path)
        path=path[:-1]
        visited[new_x][new_y]=0

    
    # Move Right:
    new_x= pos_x
    new_y=pos_y+1
    if isSafe(maze, visited, new_x, new_y):
        visited[new_x][new_y]=1
        path+="R"
        findPaths(maze, new_x, new_y, visited,ans, path)
        path=path[:-1]
        visited[new_x][new_y]=0
    

def isSafe(maze, visited, new_x, new_y):
    if 0<=new_x<n and 0<=new_y<n and visited[new_x][new_y]==0 and maze[new_x][new_y]==1:
        return True
    return False


if __name__=="__main__":
    MAZE  = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
    if MAZE[0][0]==0: # In case the rat can't land on 0,0 then we have empty answer/path
        print("")
    visited=[[0 for i in range(n)] for i in range(n)] # Create a n X n 2-D array with all nodes as 0
    visited[0][0]=1 # Mark the starting node as visited
    findPaths(MAZE, 0, 0, visited, ans, '')
    print("Path(s) is/are: ", ans)