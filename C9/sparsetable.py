#preproces 0(nlogn)
def query(l,r):
    x=log[r-l+1]
    return min(dp[x][l],dp[x][r-(1<<x)])
dp=[9,4,7,2,8,6,5,1]; n=len(dp)
log=[-1]
for i in range(1,n+1):
    log.append(log[i//2]+1)
x=log[n]
dp=[dp]+[[0]*n for i in range(x)]

for i in range(1,x+1):
    for j in range(n):
        z=1<<(i-1)
        dp[i][j]=min(dp[i-1][j],dp[i-1][min(z+j,n-1)])
#for i in dp:
#    print(*i)
while True:
    l,r=map(int,input().split())
    print(query(l,r))

