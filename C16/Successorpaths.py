def query(x,k):
    for i in range(63,-1,-1):
        if k&1<<i:
            x=dp[i][x]
    return x
log=[-1]
for i in range(10**5):
    log.append(log[i//2]+1)

link=[0, 3, 5, 7, 6, 2, 2, 1, 6, 3]
n=len(link)
x=n#log[len(link)]
dp=[[0]*n for i in range(x+1)]

for i in range(n):
    dp[0][i]=link[i]
for i in range(1,x+1):
    for j in range(n):
        z=dp[i-1][j]
        dp[i][j]=dp[i-1][z]
while True:
    a,b=map(int,input().split())
    print(query(a,b))
