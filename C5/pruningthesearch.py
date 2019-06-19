def check(grid):
    for _ in grid:
        for j in grid:
            if j==0:
                return False
    return True
#def check1_y_half():
#def check_x_half():

#def wall_hit(grid,x,y):
#    if x==0:
#
#    if x==n-1 
#    if y==0 
#    if y==n-1:



def search(c,grid,x,y):
    if c==0:
        grid[1][0]=1
        search(c+1,grid,1,0)
    elif x==n-1 and y==n-1:
        if check(grid):
            global counter
#########            counter+=1
        return 0
    #elif wall_hit(grid,x,y):
    #    return 0
    c+=1
    if y<n-1:
        if not grid[x][y+1]:
            grid[x][y+1]=c
            search(c,grid,x,y+1)
            grid[x][y+1]=0
    if y>0:
        if not grid[x][y-1]:
            grid[x][y-1]=c
            search(c,grid,x,y-1)
            grid[x][y-1]=0
    if x<n-1:
        if not grid[x+1][y]:
            grid[x+1][y]=c
            search(c,grid,x+1,y)
            grid[x+1][y]=0
    if x>0:
        if not grid[x-1][y]:
            grid[x-1][y]=c
            search(c,grid,x-1,y)
            grid[x-1][y]=0


n=7
grid=[[0]*n for i in range(n)]
grid[0][0]=1
counter=x=y=0
search(0,grid,x,y)
print(counter*2)