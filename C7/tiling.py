#doesnt work as I recall
def f(x,y,dp,t=False):
    if x==con[0]+1 and y==con[1]:
        return 1
    elif y>=con[1]:
        y=1
        x+=1
    for i in dp:
        print(*i)
    print('-----------')
    l=dp.copy()    
    if dp[x-1][y]==3 and dp[x][y-1]!=2:
        l[x][y]=1
    elif dp[x][y-1]==2 and dp[x-1][y]!=3:
        l[x][y]=4
    else:
        t=True
        l[x][y]=2
        f(x,y+1,l)
        dp[x][y]=3
        f(x,y+1,dp)
    if not t:
        f(x,y+1,l)

n,m=map(int,input().split())
l=[[0 for i in range(n+1)] for i in range(m+1)]
con=[n,m]
print(f(1,1,l))